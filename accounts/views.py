from django.shortcuts import render

# Create your views here.

def home(request):
    content = {


    }

    return render(request, 'accounts/home.html')