from django.core.management.base import BaseCommand
from calculator.models import County

# alphabetical list to make it easier for a client to find their county - improve ui
# these price values are for a few counties only - those indicated in the AAK Building permits page
# add alteration and addition of approved plan cost
# "Customization of drawing for ABT": 5000 per plan

county_data = {
    "1": {
        "Baringo": {
            "Commercial": 60,
            "Residential": 30,
            "Residential-Commercial": 30,  # est
            "Hospitals": 50,  # est
            "Educational": 20,
            "Greenhouse": 3,
            "Religious": 20,
            "Industrial": 70,
            "Solar plants": 5,  # est
            "Petrol station": 100,
            "Go downs": 100,  # est
        }
    },
    "2": {
        "Kilifi": {
            "Commercial": 60, # est
            "Residential": 30, # est
            "Residential-Commercial": 30, # est
            "Hospitals": 50, # est
            "Educational": 25, # est
            "Greenhouse": 5, # est
            "Religious": 20,  # est - calculation to be done is 50% of plinth area
            "Industrial": 65, # est
            "Solar plants": 5,  # est
            "Petrol station": 110, # est
            "Go downs": 100, # est
        }
    },
    "3": {
        "Kisii": {
            "Commercial": 60,
            "Residential": 20,
            "Residential-Commercial": 30,
            "Hospitals": 50,
            "Educational": 25,
            "Greenhouse": 5,
            "Religious": 20,  # est - calculation to be done is 50% of plinth area
            "Industrial": 65,
            "Solar plants": 5,  # est
            "Petrol station": 110,
            "Go downs": 100,
        }
    },
    "4": {
        "Laikipia": {
            "Commercial": 75,
            "Residential": 50,
            "Residential-Commercial": 50,  # est
            "Hospitals": 50,  # est
            "Educational": 30,
            "Greenhouse": 10,
            "Religious": 10,
            "Industrial": 70,
            "Solar plants": 5,  # calculated value from 20,000 per acre
            "Petrol station": 100,
            "Go downs": 100,  # est
        }
    },
    "5": {
        "Nakuru": {
            "Commercial": 60,
            "Residential": 30,
            "Residential-Commercial": 50,  # est
            "Hospitals": 50,  # est
            "Educational": 20,
            "Greenhouse": 3,
            "Religious": 20,
            "Industrial": 70,
            "Solar plants": 5,  # est
            "Petrol station": 100,
            "Go downs": 100,  # est
        }
    },
    "6": {
        "Taita-Taveta": {
            "Commercial": 40,
            "Residential": 30,
            "Residential-Commercial": 50,  # est
            "Hospitals": 50,  # est
            "Educational": 20,
            "Greenhouse": 10,
            "Religious": 20,
            "Industrial": 50,
            "Solar plants": 5,  # est
            "Petrol station": 100,
            "Go downs": 100,  # est
        }
    },
    "7": {
        "West-Pokot": {
            "Commercial": 45,
            "Residential": 40,
            "Residential-Commercial": 50,  # est
            "Hospitals": 50,  # est
            "Educational": 40,
            "Greenhouse": 5,  # est
            "Religious": 40,
            "Industrial": 45,
            "Solar plants": 5,  # est
            "Petrol station": 60,
            "Go downs": 100,  # est
        }
    },
}


class Command(BaseCommand):
    help = 'Populates the County model with data'

    def handle(self, *args, **options):

        for county_no, county_dataset in county_data.items():

            county_name = list(county_dataset.keys())[0]
            County.objects.create(county_no=int(
                county_no), county_name=county_name)
        self.stdout.write(self.style.SUCCESS(
            'County data populated successfully.'))
