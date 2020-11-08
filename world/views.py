from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WorldBorder


@login_required
def home(request):
    return render(request, 'world/home.html')


@login_required
def friends(request):
    context = {
        'countries': WorldBorder.objects.all()
    }
    return render(request, 'world/countries.html', context)

