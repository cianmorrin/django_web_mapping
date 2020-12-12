from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from . import models
from django.contrib.gis.geos import Point
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            print('yes')
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            print('no')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def update_location(request):
    try:
        user = request.user
        user_profile = models.Profile.objects.get(user__username=user)
        if not user_profile:
            raise ValueError("Can't get User details")
            
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)

        user_profile.last_location = point
        user_profile.save()

        return JsonResponse({"message": f"Set location to {point.wkt})."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
