from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from .forms import ListingForm, CommentForm
from .models import User, Listing, Bid, WatchList, Comment


def index(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="login")
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect("index")
    else:
        form = ListingForm()
    context = {"form": form}
    return render(request, "auctions/create-listing.html", context)


@login_required(login_url="login")
def details(request, pk):
    listing = Listing.objects.get(id=pk)
    if listing.active == False:
        comments = Comment.objects.filter(listing=listing).order_by('date')
        winning_bid = Bid.objects.filter(listing=listing).order_by("-price").first()
        if winning_bid:
            winner = winning_bid.user.username
            price = winning_bid.price
            owner = winning_bid.listing.owner
        else:
            winner = listing.owner
            price = listing.start_bid
            owner = listing.owner
        return render(request, "auctions/closed-listing.html", {"listing": listing, "winner": winner,
                                                                "user": request.user, "price": price,
                                                                "owner": owner, "comments": comments})
    else:
        form = CommentForm()
        comments = Comment.objects.filter(listing=listing).order_by('date')
        bids = len(Bid.objects.filter(listing=listing))
        is_watching = WatchList.objects.filter(user=request.user, listing=listing).exists()
        context = {"listing": listing, "is_watching": is_watching, "user": request.user, "form": form,
                   "comments": comments, "bids": bids}
        return render(request, "auctions/details.html", context)


@login_required(login_url="login")
def bid(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        amount = request.POST.get("bid_amount")
        if amount is None or amount == "":
            messages.error(request, "Please enter a valid amount.")
            return redirect("details", pk=pk)
        try:
            bid_amount = float(amount)
            highest_bid = Bid.objects.filter(listing=listing).order_by("-price").first()
            if highest_bid is not None and highest_bid.user == request.user:
                messages.error(request, "The current highest bid belongs to you.")
                return redirect("details", pk=pk)
            if highest_bid is not None and bid_amount <= highest_bid.price:
                messages.error(request, "Your bid must be greater than the current highest bid.")
                return redirect("details", pk=pk)
            if bid_amount < listing.start_bid:
                messages.error(request, "Your bid must be at least as large as the starting bid.")
                return redirect("details", pk=pk)
            new_bid = Bid(listing=listing, user=request.user, price=bid_amount, date=timezone.now())
            new_bid.save()
            listing.start_bid = bid_amount
            listing.save()
            messages.success(request, "Your bid has been placed.")
            return redirect("details", pk=pk)
        except ValueError:
            messages.error(request, "Please enter a valid amount.")
            return redirect("details", pk=pk)
    return render(request, "auctions/details.html", {"listing": listing})


def categories(request):
    # Aggregate the active listings by category
    categories = Listing.objects.filter(active=True).values('category').annotate(num_listings=Count('id'))

    # Pass the categories to the template
    context = {'categories': categories}
    return render(request, 'auctions/categories.html', context)


def category(request, category):
    # Retrieve the active listings in the category
    listings = Listing.objects.filter(category=category, active=True)

    # Pass the listings and category to the template
    context = {'listings': listings, 'category': category}
    return render(request, 'auctions/category.html', context)


@login_required(login_url="login")
def add_to_watchlist(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    user = request.user

    # Check if the listing is already in the watchlist
    in_watchlist = WatchList.objects.filter(listing=listing, user=user).exists()

    if not in_watchlist:
        watchlist = WatchList(listing=listing, user=user)
        watchlist.save()
        messages.success(request,"Item added to your watchlist.")
        return HttpResponseRedirect(reverse("details", args=(listing.id,)))
    else:
        # Listing is already in watchlist, so remove "Add to watchlist" button
        context = {"listing": listing, "is_watching": True, "user": request.user}
        messages.warning(request, "This item is already in your watchlist.")
        return render(request, "auctions/details.html", context)


@login_required(login_url="login")
def remove_from_watchlist(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    user = request.user
    # Check if the listing is in the user's watchlist
    watchlist_item = WatchList.objects.filter(listing=listing, user=user).first()

    if watchlist_item:
        watchlist_item.delete()
        messages.success(request, "Item removed from your watchlist.")
    else:
        messages.warning(request, "This item is not in your watchlist.")

    return HttpResponseRedirect(reverse("details", args=(listing.id,)))


@login_required(login_url="login")
def watchlist_view(request):
    watchlist_items = WatchList.objects.filter(user=request.user)
    context = {"watchlist_items": watchlist_items}
    return render(request, "auctions/watchlist.html", context)


@login_required(login_url="login")
def close_listing(request, pk):
    listing = Listing.objects.get(pk=pk)
    if request.method == "POST":
        if request.user == listing.owner:
            listing.active = False
            listing.save()
            # Notify the highest bidder
            winning_bid = Bid.objects.filter(listing=listing).order_by("-price").first()

            return redirect("details", pk=pk)

        # If the request method is not POST, render the template for confirmation
        return render(request, "auctions/closed-listing.html", {"listing": listing})


@login_required(login_url="login")
def comment(request, pk):
    if request.method == "POST":
        listing = Listing.objects.get(id=pk)
        comment_content = request.POST.get("comment_content")
        comment = Comment(user=request.user, listing=listing, comment=comment_content)
        comment.save()
    else:
        listing = Listing.objects.get(id=pk)

    comments = Comment.objects.filter(listing=listing).order_by('date')
    is_watching = WatchList.objects.filter(user=request.user, listing=listing).exists()
    return render(request, "auctions/details.html", {"listing": listing, "comments": comments,
                                                     "is_watching": is_watching, "user": request.user})


@login_required(login_url="login")
def all_closed_listings(request):
    listings = Listing.objects.filter(active=False)
    context = {"listings": listings}
    return render(request, "auctions/all-closed-listings.html", context)
