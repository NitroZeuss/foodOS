from django.contrib import admin
from .models import Recipe, RecipeCategory, RecipeBookmark, RecipeComment, RecipeIngredient, RecipeNutrition, RecipeRating  # Import your models

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name',)  # Fields to enable search functionality
    list_filter = ('created_at',)  # Fields to filter by in the admin list view

@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the admin list view
    search_fields = ('name',)  # Fields to enable search functionality

@admin.register(RecipeBookmark)
class RecipeBookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')  # Adjust fields based on your model
    search_fields = ('user__username', 'recipe__name')  # Enable search functionality
    list_filter = ('created_at',)  # Filter by creation date

@admin.register(RecipeComment)
class RecipeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'content', 'created_at')  # Adjust fields based on your model
    search_fields = ('user__username', 'recipe__name', 'content')  # Enable search functionality
    list_filter = ('created_at',)  # Filter by creation date



@admin.register(RecipeNutrition)
class RecipeNutritionAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'calories', 'protein', 'fat', 'carbohydrates')  # Adjust fields based on your model
    search_fields = ('recipe__name',)  # Enable search functionality

@admin.register(RecipeRating)
class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'rating', 'created_at')  # Adjust fields based on your model
    search_fields = ('user__username', 'recipe__name')  # Enable search functionality
    list_filter = ('rating', 'created_at')  # Filter by rating and creation date

