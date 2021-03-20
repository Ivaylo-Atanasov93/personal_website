from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import PersonalInformation


class HomePageView(ListView):
    queryset = PersonalInformation.objects.all()
    template_name = 'index.html'
