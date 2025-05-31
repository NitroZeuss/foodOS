from django.db import models
from accounts.models import CustomUser

class RecipeCategory(models.Model):
    CATEGORY_CHOICES = [
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Appetizer', 'Appetizer'),
        ('Snack', 'Snack'),
        ('Beverage', 'Beverage'),
        ('Dessert', 'Dessert'),
        ('Breakfast', 'Breakfast'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_nut_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    name = models.CharField(max_length=200)
   # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)  # Removed invalid default
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    steps = models.TextField()
    cook_time_minutes = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    cuisine = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipes')

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
