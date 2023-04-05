from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .models import User, Follow, Like
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import F
from django.db.models.signals import post_save
from .models import Post
import json
from django.core.files.storage import FileSystemStorage



def index(request):
    # Get all posts ordered by date posted (most recent first)
    all_posts = Post.objects.all().order_by('-timestamp')

    # Get post IDs that the user has liked
    likes = Like.objects.all()
    post_liked_ids = []
    post_likes_count = {}

    for post in all_posts:
        post_likes_count[post.id] = post.likes.count()
        for like in likes:
            if like.user.id == request.user.id and like.post.id == post.id:
                post_liked_ids.append(like.post.id)

    # Paginate the posts, showing 10 per page
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render index.html template with form and posts
    return render(request, "network/index.html", {"posts": page_obj, "user": request.user , "post_liked_ids": post_liked_ids, "post_likes_count": post_likes_count})


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            profile_photo = request.FILES["profile_photo"] # Get the uploaded image file
            fs = FileSystemStorage() # Create a FileSystemStorage instance
            filename = fs.save(profile_photo.name, profile_photo) # Save the uploaded image to the file system
            profile_photo_url = fs.url(filename) # Get the URL of the saved image
            user = User.objects.create_user(username, email, password, profile_photo=profile_photo_url)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def new_post(request):
    if request.method == 'GET':
        return render(request, "network/index.html")
    else:
        content = request.POST.get('content')
        post = Post(user=request.user, content=content, timestamp=timezone.now())
        post.save()
        return redirect('index')

@login_required(login_url="login")
def profile(request, username):
    # Get the requested user object
    user = get_object_or_404(User, username=username)

    # Determine if the current user is already following the requested user
    following = False
    if request.user.is_authenticated:
        following = request.user.following_set.filter(followed=user).exists()


    # Get all posts for the requested user, in reverse chronological order
    posts = user.posts.all().order_by('-timestamp')

    paginator = Paginator(posts, 10) # Show 10 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # Get the number of followers and following for the requested user
    num_following = user.following_set.count()
    num_followers = user.followed_set.count()
    ...
    # Get post IDs that the user has liked
    likes = Like.objects.all()
    post_liked_ids = []
    post_likes_count = {}

    for post in posts:
        post_likes_count[post.id] = post.likes.count()
        for like in likes:
            if like.user.id == request.user.id and like.post.id == post.id:
                post_liked_ids.append(like.post.id)

    # Render profile.html template with user's profile information and posts
    return render(request, "network/profile.html", {
        "profile_user": user,
        "num_following": num_following,
        "num_followers": num_followers,
        "following": following,
        "posts": posts,
        "user": request.user,
        "post_liked_ids": post_liked_ids,
        "post_likes_count": post_likes_count
    })


@login_required
def follow(request, username):
    # Get the user object that the current user wants to follow
    followed_user = get_object_or_404(User, username=username)

    # Check if the current user is already following the other user
    if request.user.following_set.filter(followed=followed_user).exists():
        # User is already following, redirect to profile page
        return redirect('profile', username=username)

    # Create a new Follow instance to represent the relationship
    follow = Follow.objects.create(follower=request.user, followed=followed_user)

    # Redirect back to the profile page of the user being followed
    return redirect('profile', username=username)


@login_required
def unfollow(request, username):
    # Get the user object that the current user wants to unfollow
    unfollowed_user = get_object_or_404(User, username=username)

    # Check if the current user is following the other user
    follow = request.user.following_set.filter(followed=unfollowed_user).first()
    if follow is None:
        # User is not following, redirect to profile page
        return redirect('profile', username=username)

    # Delete the Follow instance to remove the relationship
    follow.delete()

    # Redirect back to the profile page of the user being unfollowed
    return redirect('profile', username=username)

@login_required
def following(request):
    # Get a QuerySet of users that the current user is following
    following_users = request.user.following_set.all().values_list('followed_id', flat=True)

    # Get all posts made by the users that the current user is following, in reverse chronological order
    posts = Post.objects.filter(user__in=following_users).order_by('-timestamp')

    # Paginate the posts, showing 10 per page
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # Get post IDs that the user has liked
    likes = Like.objects.all()
    post_liked_ids = []
    post_likes_count = {}

    for post in posts:
        post_likes_count[post.id] = post.likes.count()
        for like in likes:
            if like.user.id == request.user.id and like.post.id == post.id:
                post_liked_ids.append(like.post.id)

    # Render index.html template with form and posts
    return render(request, "network/following.html", {"posts": page_obj, "user": request.user , "post_liked_ids": post_liked_ids, "post_likes_count": post_likes_count})


def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.content = data['content']
        edit_post.save()
        return JsonResponse({"message": "Change successful", "data": data["content"]})


def toggle_like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)

    if user.user_like.filter(post=post).exists():
        like = Like.objects.get(user=user, post=post)
        like.delete()
        Post.objects.filter(pk=post_id).update(num_likes=F('num_likes') - 1)
        post.refresh_from_db()
        message = "Like successfully removed"
    else:
        like = Like(user=user, post=post)
        like.save()
        Post.objects.filter(pk=post_id).update(num_likes=F('num_likes') + 1)
        post.refresh_from_db()
        message = "Like successfully added"

    return JsonResponse({"message": message, "likes_count": post.num_likes, "post_liked_ids": list(user.user_like.values_list("post__id", flat=True))}, status=200)


