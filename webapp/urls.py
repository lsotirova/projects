from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('search/', views.search_ingredient, name='search_ingredient'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('all-recipes', views.all_recipes, name="all-recipes"),
    path('category_selection/<str:category>', views.category_selection, name="category_selection"),
    path("toggle_my_recipes/<int:recipe_id>", views.toggle_my_recipe, name="toggle_my_recipe"),
    path("my_account_recipes", views.my_account_recipes, name="my_account_recipes"),
    path("my_plan_form", views.my_plan_form, name="my_plan_form"),
    path("my_plan_form/save_my_plan", views.save_my_plan, name="save_my_plan"),
    path("my_planner", views.my_planner, name="my_planner"),
    path("delete_recipe_from_plan/<int:plan_id>/<int:recipe_id>/", views.delete_recipe_from_plan, name="delete_recipe_from_plan")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)