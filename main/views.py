from django.shortcuts import render
from .models import Person, Status
from .serializers import PersonSerializer, StatusSerializer
from rest_framework.generics import *


class StatusListCreate(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class PersonsListCreate(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
