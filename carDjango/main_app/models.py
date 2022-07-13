from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CARS = (
    ('E', 'V8'),
    ('T', 'V10'),
    ('EL','V12'),
    ('S', 'V16')
)

def __init__(self, car, brand, description, year):
  self.car = car
  self.brand = brand
  self.description = description
  self.year = year


class Car(models.Model):
  car= models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  year = models.IntegerField()
  
  
class Specs(models.Model):
  mpg = models.CharField(max_length=6)
  horsepower = models.CharField(max_length=6)

  # def __str__(self):
  #       return self.car
      
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
    

      
  def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})
  
  def __str__(self):
    return f"{self.get_specs_display()} on {self.mpg}"
  
class Meta:
  ordering = ['-mpg']


  

  

    