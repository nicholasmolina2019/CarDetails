from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import SpecsForm


def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
 

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  cars = Car.objects.get(id=car_id)
  specs_form = SpecsForm()
  return render(request, 'cars/detail.html', { 
    'cars': cars, 'specs_form': specs_form
                                              
  })

def add_specs(request, car_id):
  form = SpecsForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_specs = form.save(commit=False)
    new_specs.car_id = car_id
    new_specs.save()
  return redirect('/cars/', cat_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = ['car', 'brand', 'description', 'year']
  success_url = '/cars/'
  
  
class CarUpdate(UpdateView):
  model = Car
  fields = ['car', 'brand', 'description', 'year']
 
class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'