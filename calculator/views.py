from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import County
from .serializers import CountySerializer

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