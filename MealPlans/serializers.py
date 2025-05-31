from rest_framework import serializers
from .models import DailyMeal, WeeklyMealPlan

class DailyMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMeal
        fields = '__all__'

class WeeklyMealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyMealPlan
        fields = '__all__'
