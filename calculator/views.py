from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import County, ProjectType
from .serializers import CountySerializer, ProjectTypeSerializer
from .management.commands.populate_counties import county_data

# Create your views here.


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


@api_view(['GET'])
def project_type_list(request):
    try:
        project_types = ProjectType.objects.all()

    except ProjectType.DoesNotExist:
        return Response(
            {"error": "There are no projects listed"},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = ProjectTypeSerializer(project_types, many=True)
    return Response(
        {"message": "Projects retrieved succesfully", "results": serializer.data},
        status=status.HTTP_200_OK,
    )


@api_view(['POST'])
def calculate_cost(request):
    if request.method == 'POST':
        project_size = request.data.get('size')
        county_name = request.data.get('county')
        project_type_name = request.data.get('projectType')
        construction_cost = request.data.get('cost')

        for county_no, county_item in county_data.items():
            # Check if the county name exists in the current county_item
            if county_item.get(county_name):
                price = county_item[county_name].get(project_type_name)
                if price is not None:
                    
                    application_form = 1000
                    site_board_application = 1500
                    site_board_license = 15000
                    site_board = site_board_application + site_board_license
                    
                    arch_building_cost = (int(project_size)) * price
                    building_permit_cost = arch_building_cost + application_form + site_board

                context = {
                    'architectural plans cost': int(arch_building_cost),
                    'total estimated cost for a building permit': int(building_permit_cost),
                }

                return Response(
                    {"message": "Buildling permit cost calculated successfully!",
                        "context": context},
                    status=status.HTTP_200_OK,
                )
            # handle errors correctly
    else:
        return Response(
            {"error": "Invalid request method"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
