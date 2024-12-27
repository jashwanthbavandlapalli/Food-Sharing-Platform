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
    path('donate/donate-form/', views.donate_form, name='donate_form'),
    path('submit-donate-form/', views.submit_donate_form, name='submit_donate_form'),
    path('donate/donate-form/kindness-page/', views.kindness_page, name='kindness_page'),
    path('request/request-form/', views.request_form, name='request_form'),
    path('submit-request-form/', views.submit_request_form, name='submit_request_form'),

]