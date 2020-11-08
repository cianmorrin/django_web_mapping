from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='world-home'),
    path('cities/', views.friends, name='world-countries'),
]