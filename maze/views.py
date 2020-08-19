from django.shortcuts import render, redirect
from django.views import generic
from . import views
from django.urls import path
from django.shortcuts import render
from .models import function


# Create your views here.
def homepage(request):
    # projects = Project.objects.all()  # if logic is required -> use a controller
    return render(request, 'maze/index.html')