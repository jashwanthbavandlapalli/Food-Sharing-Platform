from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
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
def request_food(request):
    return render(request, 'request_food.html')
def search_food(request):
    return render(request, 'search_food')
def find_us(request):
    return render(request, 'find_us.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})
                            