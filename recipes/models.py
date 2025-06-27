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
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recipes',
        null=True,
        blank=True,
        help_text="User who created this recipe"
    )
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    steps = models.TextField(help_text="Instructions in plain text or markdown")
    cook_time_minutes = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    cuisine = models.CharField(max_length=100, blank=True, help_text="e.g. Indian, Italian")
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'RecipeCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recipes'
    )

    # 🔥 New fields for personalized compatibility
    suitable_for_diet_types = models.ManyToManyField(
        'DietType',
        blank=True,
        help_text="Which diets this recipe suits e.g. Vegan, Keto"
    )
    contains_nuts = models.BooleanField(default=False)
    contains_gluten = models.BooleanField(default=False)
    contains_dairy = models.BooleanField(default=False)

    taste_tags = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g. spicy, tangy, sweet"
    )

    calories = models.PositiveIntegerField(null=True, blank=True, help_text="Approximate calorie content")

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"

class DietType(models.Model):
    name = models.CharField(
        max_length=30,
        choices=CustomUser.DIET_TYPE_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()
