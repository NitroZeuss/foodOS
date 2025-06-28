from rest_framework import serializers
from .models import Ingredient, Recipe, RecipeIngredient, RecipeCategory, DietType, RecipeRating, RecipeBookmark, RecipeComment

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = '__all__'

class DietTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietType
        fields = '__all__'

class RecipeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRating
        fields = ['recipe', 'user', 'rating', 'comment', 'created_at']

class RecipeBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeBookmark
        fields = ['user', 'recipe', 'created_at']

class RecipeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeComment
        fields = ['recipe', 'user', 'content', 'created_at']

