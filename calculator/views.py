from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import  CalculatorForm
from .models import County
from .serializers import CountySerializer

# return JSON encoded responses
from django.http import JsonResponse
# Create your views here.
@api_view(['GET', 'POST'])
def calculator(request):
    if request.method == 'GET':
        form = CalculatorForm()
             
        # serialize the form fields
        form_fields = { # dictionary
            'project_size': form['project_size'].value(),
            'type_of_project': form['type_of_project'].value(),
            'county': form['county'].value(),
            'total_cost_of_construction_project': form['total_cost_of_construction_project'].value()
        }
        return JsonResponse({'form': form_fields})
    
    elif request.method == 'POST':
        form = CalculatorForm(request.data)
        if form.is_valid():
            total_size = form.cleaned_data['project_size']
            project_type_charges = form.cleaned_data['type_of_project']
            county_charges = form.cleaned_data['county']
            total_cost = form.cleaned_data['total_cost_of_construction_project']
            # calculate the total amount:
                # folio registry number search 150
                # survey plan 650
                # nema approval fee 10000
                # 21000 per sqm:
                    # building plan approval fee 1% of the estimated cost of construction
                    # construction sin board fee 25000
                    # application fee 5000
                    # inspection of building file 5000
                    # occupation certificate 5000
                # nca levy 0.5% of the total cost of construction
            
            building_permit = ((total_size*21000) + 10800)
            nca_levy = (0.005 * total_cost)
            # use control flow to render results when the nca_levy is calculated and when it is omitted since it is an optional field
            approvals_cost = ((total_size*21000) + 10800 + nca_levy)
                
            # the rate is different for each project type
            # the rate is different in every county
            # create context
            context = {
                'approvals_cost': int(approvals_cost),
                'nca_levy': int(nca_levy),
                'building_permit': int(building_permit)
            }
            return JsonResponse(context)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)

@api_view(['GET'])
def county_list(request):
    try:
      counties = County.objects.all()

    except County.DoesNotExist:
        return Response(
            {"error": "There are no counties listed"},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = CountySerializer(counties, many=True)
    return Response(
        {"message": "Counties retrieved successfully", "results": serializer.data},
        status=status.HTTP_200_OK,
    )