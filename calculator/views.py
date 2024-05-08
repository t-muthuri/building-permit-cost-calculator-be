from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import County, ProjectType
from .serializers import CountySerializer, ProjectTypeSerializer

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
        county_no = request.data.get('county')
        project_type_no = request.data.get('projectType')
        construction_cost = request.data.get('cost')
        
        nca_levy = (0.005 * int(construction_cost))
        
        return Response(
            {"message": "Approval cost calculated successfully!"},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"error": "Invalid request method"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )