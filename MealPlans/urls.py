from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyMealViewSet, WeeklyMealPlanViewSet

router = DefaultRouter()
router.register(r'daily-meals', DailyMealViewSet)
router.register(r'weekly-plans', WeeklyMealPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
