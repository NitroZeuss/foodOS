from rest_framework import viewsets
from .models import DailyMeal, WeeklyMealPlan
from .serializers import DailyMealSerializer, WeeklyMealPlanSerializer
from rest_framework import permissions

class DailyMealViewSet(viewsets.ModelViewSet):
    queryset = DailyMeal.objects.all()
    serializer_class = DailyMealSerializer
    permission_classes = [permissions.IsAuthenticated]  

class WeeklyMealPlanViewSet(viewsets.ModelViewSet):
    queryset = WeeklyMealPlan.objects.all()
    serializer_class = WeeklyMealPlanSerializer
    permission_classes = [permissions.IsAuthenticated]