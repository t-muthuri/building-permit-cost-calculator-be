from django.core.management.base import BaseCommand
from calculator.models import County, ProjectType

class Command(BaseCommand):
    help = 'Populates the County and ProjectType models with data'

    def handle(self, *args, **options):
      
        # alphabetical list to make it easier for a client to find their county - improve ui
        # these price values are for a few counties only - those indicated in the AAK Building permits page
        # add alteration and addition of approved plan cost
        # "Customization of drawing for ABT": 5000 per plan
        
        county_data = {
          "001": {
            "Baringo": {
              "Commercial": 60,
              "Residential": 30,
              "Residential-Commercial": 30, # est
              "Hospitals": 50, # est
              "Educational": 20,
              "Greenhouse": 3,
              "Religious": 20,
              "Industrial": 70,
              "Solar plants": 5, # est
              "Petrol station": 100,
              "Go downs": 100, # est
            }
          },
          "002": {
            "Kilifi": 30
          },
          "003": {
            "Kisii": {
              "Commercial": 60,
              "Residential": 20,
              "Residential-Commercial": 30,
              "Hospitals": 50,
              "Educational": 25,
              "Greenhouse": 5,
              "Religious": 20, # est - calculation to be done is 50% of plinth area
              "Industrial": 65,
              "Solar plants": 5, # est
              "Petrol station": 110,
              "Go downs": 100,
            }
          },
          "004": {
            "Laikipia": {
              "Commercial": 75,
              "Residential": 50,
              "Residential-Commercial": 50, # est
              "Hospitals": 50, # est
              "Educational": 30,
              "Greenhouse": 10,
              "Religious": 10,
              "Industrial": 70,
              "Solar plants": 5, # calculated value from 20,000 per acre
              "Petrol station": 100,
              "Go downs": 100, # est
            }
          },
          "005": {
            "Nakuru": {
              "Commercial": 60,
              "Residential": 30,
              "Residential-Commercial": 50, # est
              "Hospitals": 50, # est
              "Educational": 20,
              "Greenhouse": 3,
              "Religious": 20,
              "Industrial": 70,
              "Solar plants": 5, # est
              "Petrol station": 100,
              "Go downs": 100, # est
            }
          },
          "006": {
            "Taita-Taveta": {
              "Commercial": 40,
              "Residential": 30,
              "Residential-Commercial": 50, # est
              "Hospitals": 50, # est
              "Educational": 20,
              "Greenhouse": 10,
              "Religious": 20,
              "Industrial": 50,
              "Solar plants": 5, # est
              "Petrol station": 100,
              "Go downs": 100, # est
            }
          },
          "007": {
            "West-Pokot": {
              "Commercial": 45,
              "Residential": 40,
              "Residential-Commercial": 50, # est
              "Hospitals": 50, # est
              "Educational": 40,
              "Greenhouse": 5, # est
              "Religious": 40,
              "Industrial": 45,
              "Solar plants": 5, # est
              "Petrol station": 60,
              "Go downs": 100, # est
            }
          },
        }
        
        for county_no, county_data in county_data.items():
            county_name = list(county_data.keys())[0]
            county_instance = County.objects.create(county_no=county_no, county_name=county_name)
            
            if isinstance(county_data[county_name], int):  # If the value is an integer
                continue  # Skip because there's no project data for this county
            else:
                for project_name, project_price in county_data[county_name].items():
                    project_instance = ProjectType.objects.create(project_name=project_name, project_price=project_price, county=county_instance)

        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))