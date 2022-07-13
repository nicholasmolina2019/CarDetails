
from django.forms import ModelForm
from .models import Specs

class SpecsForm(ModelForm):
  class Meta:
    model = Specs
    fields = ['mpg', 'horsepower']