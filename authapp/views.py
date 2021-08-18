from django.shortcuts import render
from .models import Students
from .serializers import StudentSeri
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSeri

    permission_classes = (IsAuthenticated,)
