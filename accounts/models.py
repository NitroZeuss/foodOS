from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # BASIC PROFILE
    age = models.PositiveIntegerField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True)

    # DIET PREFERENCES
    DIET_TYPE_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('non_vegetarian', 'Non-Vegetarian'),
        ('pescatarian', 'Pescatarian'),
        ('keto', 'Keto'),
        ('paleo', 'Paleo'),
        ('open', 'Open to All'),
    ]
    diet_type = models.CharField(max_length=30, choices=DIET_TYPE_CHOICES, default='open')

    # MEDICAL / RESTRICTIONS
    has_diabetes = models.BooleanField(default=False)
    is_lactose_intolerant = models.BooleanField(default=False)
    is_gluten_intolerant = models.BooleanField(default=False)
    is_allergic_to_nuts = models.BooleanField(default=False)
    other_allergies = models.TextField(blank=True)

    # INGREDIENT & TASTE PREFERENCES
    favorite_ingredients = models.TextField(blank=True, help_text="Comma-separated e.g. 'garlic, cheese, basil'")
    disliked_ingredients = models.TextField(blank=True, help_text="Comma-separated e.g. 'onion, chili'")
    taste_profile = models.CharField(max_length=255, blank=True, help_text="e.g. spicy, sweet, tangy, bland")

    # CUISINE & MEAL PREFERENCES
    favorite_cuisines = models.TextField(blank=True, help_text="e.g. Indian, Thai, Italian")
    avoid_cuisines = models.TextField(blank=True, help_text="e.g. Chinese, Continental")
    preferred_meal_times = models.JSONField(default=dict, blank=True, help_text='e.g. {"breakfast": "08:00", "lunch": "13:00", "dinner": "20:00"}')

    # FITNESS & GOALS
    fitness_goal = models.CharField(max_length=100, blank=True, help_text="e.g. weight loss, muscle gain, maintenance")
    daily_calorie_limit = models.PositiveIntegerField(null=True, blank=True)
    meal_frequency = models.PositiveIntegerField(default=3, help_text="How many meals they want daily")

    # ANALYTICS & FEEDBACK
    most_liked_recipes = models.ManyToManyField("recipes.Recipe", blank=True, related_name='liked_by')
    most_disliked_recipes = models.ManyToManyField("recipes.Recipe", blank=True, related_name='disliked_by')
    feedback_notes = models.TextField(blank=True, help_text="User feedback for personalized AI analysis")

    def __str__(self):
        return self.username
