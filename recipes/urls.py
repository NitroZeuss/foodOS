from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet, RecipeCategoryViewSet, DietTypeViewSet, RecipeRatingViewSet, RecipeBookmarkViewSet, RecipeCommentViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipe-categories', RecipeCategoryViewSet)
router.register(r'diet-types', DietTypeViewSet)
router.register(r'recipe-ratings', RecipeRatingViewSet)
router.register(r'recipe-bookmarks', RecipeBookmarkViewSet)
router.register(r'recipe-comments', RecipeCommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
 