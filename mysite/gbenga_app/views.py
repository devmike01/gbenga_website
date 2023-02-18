from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
