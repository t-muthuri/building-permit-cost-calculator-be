from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def crazy_enough(request):
    return Response({'message': 'It is those that are CRAZY ENOUGH to think that they can change the world who actually do.'})