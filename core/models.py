from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.date}"


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(help_text="Carga em kg")

    def __str__(self):
        return f"{self.name} ({self.sets}x{self.reps} - {self.weight}kg)"


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=50)  # Ex: café da manhã, almoço

    def __str__(self):
        return f"{self.meal_type} - {self.date}"


class FoodItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    quantity = models.FloatField(help_text="Quantidade em gramas")
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.quantity}g)"


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(help_text="Peso em kg")
    arm = models.FloatField(help_text="Braço em cm")
    waist = models.FloatField(help_text="Cintura em cm")
    hips = models.FloatField(help_text="Quadril em cm")

    def __str__(self):
        return f"{self.date} - {self.weight}kg"
