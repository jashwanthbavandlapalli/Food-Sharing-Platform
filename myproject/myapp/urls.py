from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.base, name='base.html'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('donate/',views.donate_food, name='donate_food'),
    path('request/', views.request_food, name='request_food'),
    path('',views.search_food, name='search_food'),
    path('find_us/',views.find_us, name='find_us'),
]