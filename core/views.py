from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workout, Exercise, Meal, FoodItem, Progress
from .serializers import WorkoutSerializer, ExerciseSerializer, MealSerializer, FoodItemSerializer, ProgressSerializer
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.functional import SimpleLazyObject

class AuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        return super().parse_body(request)

    def get_context(self, request):
        context = super().get_context(request)

        def get_user():
            user_auth_tuple = JWTAuthentication().authenticate(request)
            return user_auth_tuple[0] if user_auth_tuple else None

        context.user = SimpleLazyObject(get_user)
        return context
    
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
