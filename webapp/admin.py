from django.contrib import admin
from .models import User, Ingredient, Category, Recipe, MyRecipes, MyPlan
# Register your models here.
admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(MyRecipes)
admin.site.register(MyPlan)