from django.shortcuts import render
from .forms import RegisterFrom


# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
    else: 
        form = RegisterFrom()
    
    return render(request, 'registration/sign_up.html', {"form": form})