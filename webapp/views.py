from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Recipe, Ingredient, Category, MyRecipes, MyPlan
from .models import User
import markdown
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from itertools import groupby
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator


def index(request):
    ingredients = Ingredient.objects.all()[:10]
    categories = Category.objects.all()
    return render(request, "webapp/index.html", {"ingredients": ingredients, "categories": categories})

def all_recipes(request):
    categories = Category.objects.all()
    category_id = request.POST.get('category')

    if category_id:
        recipes = Recipe.objects.filter(category__id=category_id)
    else:
        recipes = Recipe.objects.all()

    paginator = Paginator(recipes, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "webapp/all-recipes.html", {"page_obj": page_obj, "categories": categories})


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
            return render(request, "webapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "webapp/login.html")


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
            return render(request, "webapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "webapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "webapp/register.html")


def search_ingredient(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        ingredient_ids = request.POST.getlist('ingredients')
        
        # Process the search query and ingredient IDs as needed
        recipes = Recipe.objects.filter(ingredients__id__in=ingredient_ids).distinct()
        recipes2 = Recipe.objects.filter(ingredients__ingredient_name__icontains=query).distinct()
        context = {'recipes': recipes, 'recipes2': recipes2}
        return render(request, 'webapp/search-results.html', context)


def category_selection(request, category):
    categories = Category.objects.all()
    selected_category = get_object_or_404(Category, category_name=category)
    recipes = Recipe.objects.filter(category=selected_category)
    return render(request, "webapp/category.html", {"recipes": recipes, "categories": categories, "selected_category":selected_category})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.directions = markdown.markdown(recipe.directions)
    all_recipes = MyRecipes.objects.all()
    recipe_liked_ids = []
    for my_recipe in all_recipes:
        if my_recipe.user.id == request.user.id and my_recipe.recipe.id == recipe.id:
            recipe_liked_ids.append(my_recipe.recipe.id)
    context = {'recipe': recipe, "recipe_liked_ids": recipe_liked_ids}
    return render(request, 'webapp/recipe-detail.html', context)


def toggle_my_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = User.objects.get(pk=request.user.id)

    if user.user_recipe.filter(recipe=recipe).exists():
        my_recipe = MyRecipes.objects.get(user=user, recipe=recipe)
        my_recipe.delete()
        message = "Like successfully removed"
    else:
        my_recipe = MyRecipes(user=user, recipe=recipe)
        my_recipe.save()
        message = "Like successfully added"

    # Get the list of recipe IDs liked by the user
    recipe_liked_ids = list(user.user_recipe.values_list("recipe__id", flat=True))

    print(recipe_liked_ids)
    return JsonResponse(
        {"message": message, "recipe_liked_ids": recipe_liked_ids},
        status=200
    )

@login_required(login_url='login')
def my_account_recipes(request):
    categories = Category.objects.all()
    user = User.objects.get(username=request.user)
    category_id = request.POST.get('category')
    
    if category_id:
        recipes = MyRecipes.objects.filter(user=user, recipe__category__id=category_id)
    else:
        recipes = MyRecipes.objects.filter(user=user)

    return render(request, "webapp/my-account.html", {"recipes": recipes, "categories": categories})


@login_required(login_url='login')
def my_plan_form(request):
    user = User.objects.get(username=request.user)
    categories = Category.objects.all()

    recipes_by_category = {}
    for category in categories:
        recipes_by_category[category] = MyRecipes.objects.filter(user=user, recipe__category=category)

    return render(request, "webapp/my-plan-form.html", {"recipes_by_category": recipes_by_category})


@login_required(login_url='login')
def save_my_plan(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        recipe_ids = request.POST.getlist('myRecipes')

        # Retrieve the selected recipes from the database
        recipes = Recipe.objects.filter(id__in=recipe_ids)

        # Check if a plan for the given date already exists
        my_plan = MyPlan.objects.filter(user=request.user, date=date).first()

        if my_plan:
            # If a plan exists, add the selected recipes to it
            my_plan.recipes.add(*recipes)
        else:
            # If no plan exists, create a new MyPlan instance
            my_plan = MyPlan(user=request.user, date=date)
            my_plan.save()
            my_plan.recipes.set(recipes)

        # Redirect to a success page or any other desired action
        return redirect('my_planner')

    return render(request, 'webapp/my-plan-form.html')



@login_required(login_url='login')
def my_planner(request):
    user = request.user
    plans = MyPlan.objects.filter(user=user).order_by('date')

    grouped_plans = []
    for date, plan_group in groupby(plans, key=lambda plan: plan.date):
        grouped_plans.append({'date': date, 'plans': list(plan_group)})

    return render(request, 'webapp/my-planner.html', {'grouped_plans': grouped_plans})


@login_required(login_url='login')
def delete_recipe_from_plan(request, plan_id, recipe_id):
    if request.method == 'POST':
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            my_plan = MyPlan.objects.get(id=plan_id, user=request.user)
            my_plan.recipes.remove(recipe)

            # Check if the plan has any remaining recipes
            if my_plan.recipes.count() == 0:
                # If no recipes left, delete the plan
                plan_date = my_plan.date.strftime("%Y-%m-%d")  # Convert date to string
                my_plan.delete()

                # Return the plan date in the response
                return JsonResponse({"message": "Recipe deleted successfully.", "date": plan_date})

            # Return success message without the plan date
            return JsonResponse({"message": "Recipe deleted successfully."})

        except (Recipe.DoesNotExist, MyPlan.DoesNotExist):
            return HttpResponseBadRequest("Recipe or plan not found.")

    return HttpResponseBadRequest("Invalid request method.")
