from django.contrib import admin
from .models import Recipe, RecipeCategory  # Import your model

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