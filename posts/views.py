from django.shortcuts import render
from .models import post

# Create your views here.

def home(request):
    return render(request, 'post/home.html')
