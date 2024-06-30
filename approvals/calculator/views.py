from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import County, ProjectType
from .serializers import CountySerializer, ProjectTypeSerializer
from .management.commands.populate_counties import county_data

# Create your views here.
