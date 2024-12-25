from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import DonationForm
from .models import Orphanage


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")

def base(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def donate_food(request):
    return render(request, 'donate_food.html')

def donate_form(request):
    return render(request, 'donate_form.html')

def submit_donate_form(request):
    if request.method == 'POST':
        donation_success = True
        if donation_success:
            return redirect('kindness_page') 
    return render(request, 'donation_form.html', {'donation_success': donation_success})

def kindness_page(request):
    return render(request, 'kindness_page.html')


def request_food(request):
    return render(request, 'request_food.html')

def search_food(request):
    return render(request, 'search_food')

def find_us(request):
    return render(request, 'find_us.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after registration
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('base')

