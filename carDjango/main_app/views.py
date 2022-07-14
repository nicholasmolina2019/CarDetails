from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Photo
from .forms import SpecsForm

import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'car-detail-nick'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


@login_required
def cars_detail(request, car_id):
    cars = Car.objects.get(id=car_id)
    specs_form = SpecsForm()
    return render(request, 'cars/detail.html', {
        'cars': cars, 'specs_form': specs_form

    })


@login_required
def add_specs(request, car_id):
    form = SpecsForm(request.POST)
    if form.is_valid():

        new_specs = form.save(commit=False)
        new_specs.car_id = car_id
        new_specs.save()
    return redirect('detail', car_id=car_id)


@login_required
def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', car_id=car_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['car', 'brand', 'year', 'description']
    success_url = '/cars/'

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin,UpdateView):
    model = Car
    fields = ['car', 'brand', 'description', 'year']


class CarDelete(LoginRequiredMixin,DeleteView):
    model = Car
    success_url = '/cars/'
