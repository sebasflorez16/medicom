from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def projects(request):
    return render(request, 'core/projects.html')

def exam_profile(request):
    return render(request, 'core/exam_profile.html')

def exam_requeriments(request):
    return render(request, 'core/exam_requeriments.html')

def about(request):
    return render(request, 'core/about.html')
