from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='world-home'),
    path('countries/', views.friends, name='world-countries'),
]