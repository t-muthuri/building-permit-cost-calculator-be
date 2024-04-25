from django.shortcuts import render
# import the generic view class that gives access to the CRUD functions
from django.views import View
from .forms import  CalcForm

# Create your views here.
class Index(View):
    def get(self, request):
        form = CalcForm() # render an empty form
        return render(request, 'calc/index.html', {'form': form})

    def post(self, request):
        pass