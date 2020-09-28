from django.contrib import admin
from django.urls import path
from website import views #Manually

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('services', views.services, name = 'services'),
    path('mllearn', views.mllearn, name = 'mllearn'),
    path('robot', views.robot, name = 'robot'),
    path('basicPy', views.basicPy, name = 'basicPy'),
    
]
