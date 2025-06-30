from django.db import models
from cloudinary.models import CloudinaryField
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
    image = CloudinaryField(
        'image',
        help_text="Main image of the recipe. Required."
    )
    video = CloudinaryField(
        'video',
        resource_type='video',
        blank=True,
        null=True,
        help_text="Optional video showing how to prepare the recipe"
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

class RecipeRating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipe_ratings')
    rating = models.PositiveIntegerField(default=0, help_text="Rating from 1 to 5")
    comment = models.TextField(blank=True, help_text="Optional comment about the recipe")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.name} {self.rating}/5"

class RecipeBookmark(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookmarks')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} bookmarked {self.recipe.name}"

class RecipeComment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipe_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.recipe.name}"

class RecipeNutrition(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='nutrition')
    calories = models.PositiveIntegerField(null=True, blank=True, help_text="Approximate calorie content")
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Protein content in grams")
    fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Fat content in grams")
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Carbohydrates content in grams")

    def __str__(self):
        return f"Nutrition info for {self.recipe.name}"
