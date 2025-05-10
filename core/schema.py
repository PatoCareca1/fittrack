import graphene
from graphene_django.types import DjangoObjectType
from .models import Workout
from django.contrib.auth.models import User

class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ("id", "name", "date", "user")


class Query(graphene.ObjectType):
    all_workouts = graphene.List(WorkoutType)

    def resolve_all_workouts(self, info):
        user = info.context.user
        if user.is_authenticated:
            return Workout.objects.filter(user=user)
        return Workout.objects.none()


class CreateWorkout(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        date = graphene.types.datetime.Date(required=True)

    workout = graphene.Field(WorkoutType)

    def mutate(self, info, name, date):
        print("Token recebido:", info.context.META.get("HTTP_AUTHORIZATION"))
        print("Usuário autenticado:", info.context.user)

        user = info.context.user
        if not user.is_authenticated:
            if not user.is_authenticated:
                raise Exception("Authentication required")
        workout = Workout.objects.create(user=user, name=name, date=date)
        return CreateWorkout(workout=workout)


class Mutation(graphene.ObjectType):
    create_workout = CreateWorkout.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
