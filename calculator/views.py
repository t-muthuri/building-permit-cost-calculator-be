from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import  CalculatorForm
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def calculator(request):
    form = CalculatorForm()

    form_fields = {
        'project_size': form['project_size'].value(),
        'type_of_project': form['type_of_project'].value(),
        'county': form['county'].value(),
        'total_cost_of_construction_project': form['total_cost_of_construction_project'].value()
    }
    return JsonResponse({'form': form_fields})