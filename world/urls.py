from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='world-home'),
    path('friends/', views.friends, name='world-friends'),
]