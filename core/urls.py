from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.rest_views import WorkoutViewSet, ExerciseViewSet, MealViewSet, FoodItemViewSet, ProgressViewSet
from .views import json_views

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'meals', MealViewSet)
router.register(r'fooditems', FoodItemViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('json/workouts/', json_views.workout_list, name='json_workout_list'),
    path('json/workouts/<int:workout_id>/', json_views.workout_detail, name='json_workout_detail'),
]