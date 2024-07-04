from django.core.management.base import BaseCommand
from calculator.models import ProjectType

class Command(BaseCommand):
    help = 'Populates the ProjectType model with data'

    def handle(self, *args, **options):
        
        project_type_data = {
          "001": "Commercial",
          "002": "Residential",
          "003": "Residential-Commercial",
          "005": "Hospitals",
          "006": "Educational",
          "007": "Greenhouse",
          "008": "Religious",
          "009": "Industrial",
          "010": "Solar plants",
          "011": "Petrol station",
          "012": "Go downs"
        }
        
        for project_type_no, project_type_name in project_type_data.items():
            ProjectType.objects.create(project_type_no=int(project_type_no), project_type_name=project_type_name)
            
        self.stdout.write(self.style.SUCCESS('Project type data populated successfully.'))