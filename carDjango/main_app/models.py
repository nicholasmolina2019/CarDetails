from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# Add the Cat class & list and view function below the imports

# Add the Cat class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, car, brand, description, year):
    self.car = car
    self.brand = brand
    self.description = description
    self.year = year

cars = [
  Car('La Ferrari', 'Ferrari', 'Holy Trinity', 2013),
  Car('La Ferrari', 'Ferrari', 'Holy Trinity', 2013),
  Car('La Ferrari', 'Ferrari', 'Holy Trinity', 2013),
]

year = models.IntegerField()

def __str__(self):
        return self.car

    
class Car(models.Model):
  car= models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  year = models.IntegerField()
  
    
    