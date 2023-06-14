from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Ingredient(models.Model):
    ingredient_name = models.TextField()

    def __str__(self):
        return f"{self.ingredient_name}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.category_name}"

class Recipe(models.Model):
    name = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    img_url = models.TextField()
    cook_time = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="recipes")

    def get_recipes_by_ingredient(self, ingredient_name):
        return Recipe.objects.filter(ingredients__ingredient_name__icontains=ingredient_name)

    def get_recipes_by_category(self, category_id):
        return self.category.filter(id=category_id)

    
    def __str__(self):
        return f"{self.name}"

class MyRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="post_recipe")
    
    def __str__(self):
        return f"{self.user} liked {self.recipe}"


class MyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_plans')
    date = models.DateField()
    recipes = models.ManyToManyField(Recipe, related_name='my_plans')

    def __str__(self):
        return f'MyPlan - Date: {self.date}'