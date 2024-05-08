from rest_framework import serializers
from .models import County
from .models import ProjectType

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('county_no', 'county_name')
        
class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ('project_type_name', 'project_type_no')