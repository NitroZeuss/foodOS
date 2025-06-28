from rest_framework import viewsets
from .models import Ingredient, Recipe, RecipeCategory, DietType, RecipeRating, RecipeBookmark, RecipeComment
from .serializers import IngredientSerializer, RecipeSerializer, RecipeCategorySerializer, DietTypeSerializer, RecipeRatingSerializer, RecipeBookmarkSerializer, RecipeCommentSerializer
from rest_framework import permissions


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RecipeCategoryViewSet(viewsets.ModelViewSet):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DietTypeViewSet(viewsets.ModelViewSet):
    queryset = DietType.objects.all()
    serializer_class = DietTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RecipeRatingViewSet(viewsets.ModelViewSet):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RecipeBookmarkViewSet(viewsets.ModelViewSet):
    queryset = RecipeBookmark.objects.all()
    serializer_class = RecipeBookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RecipeCommentViewSet(viewsets.ModelViewSet):
    queryset = RecipeComment.objects.all()
    serializer_class = RecipeCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]