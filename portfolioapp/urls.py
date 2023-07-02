from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discuss-idea', views.send_message, name='send_message')
]