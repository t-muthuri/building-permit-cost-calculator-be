from django.core.management.base import BaseCommand
from calculator.models import County

class Command(BaseCommand):
    help = 'Populates the County model with data'

    def handle(self, *args, **options):
        # county_data = {
        #   "001": "Mombasa",
        #   "002": "Kwale",
        #   "003": "Kilifi",
        #   "004": "Tana River",
        #   "005": "Lamu",
        #   "006": "Taita-Taveta",
        #   "007": "Garissa",
        #   "008": "Wajir",
        #   "009": "Mandera",
        #   "010": "Marsabit",
        #   "011": "Isiolo",
        #   "012": "Meru",
        #   "013": "Tharaka-Nithi",
        #   "014": "Embu",
        #   "015": "Kitui",
        #   "016": "Machakos",
        #   "017": "Makueni",
        #   "018": "Nyandarua",
        #   "019": "Nyeri",
        #   "020": "Kirinyaga",
        #   "021": "Murang'a",
        #   "022": "Kiambu",
        #   "023": "Turkana",
        #   "024": "West Pokot",
        #   "025": "Samburu",
        #   "026": "Trans-Nzoia",
        #   "027": "Uasin Gishu",
        #   "028": "Elgeyo-Marakwet",
        #   "029": "Nandi",
        #   "030": "Baringo",
        #   "031": "Laikipia",
        #   "032": "Nakuru",
        #   "033": "Narok",
        #   "034": "Kajiado",
        #   "035": "Kericho",
        #   "036": "Bomet",
        #   "037": "Kakamega",
        #   "038": "Vihiga",
        #   "039": "Bungoma",
        #   "040": "Busia",
        #   "041": "Siaya",
        #   "042": "Kisumu",
        #   "043": "Homa Bay",
        #   "044": "Migori",
        #   "045": "Kisii",
        #   "046": "Nyamira",
        #   "047": "Nairobi"
        #   }
        
        # alphabetical list to make it easier for a client to find their county - improve ui
        # these price values are for residential projects only
        county_data = {
          "001": {"name": "Baringo", "price": 30},
          "002": {"name": "Bomet", "price": 15}, # est
          "003": {"name": "Bungoma", "price": 10}, # est
          "004": {"name": "Busia", "price": 10}, #est
          "005": {"name": "Elgeyo-Marakwet", "price": 10}, #est
          "006": {"name": "Embu", "price": 10}, #est
          "007": {"name": "Garissa", "price": 5}, # est
          "008": {"name": "Homa Bay", "price": 5}, # est
          "009": {"name": "Isiolo", "price": 10}, # est
          "010": {"name": "Kajiado", "price": 5}, # est
          "011": {"name": "Kakamega", "price": 10}, # est
          "012": {"name": "Kericho", "price": 10}, # est
          "013": {"name": "Kiambu", "price": 50}, # est
          "014": {"name": "Kilifi", "price": 30},
          "015": {"name": "Kirinyaga", "price": 7}, # est
          "016": {"name": "Kisii", "price": 20},
          "017": {"name": "Kisumu", "price": 10}, # est
          "018": {"name": "Kitui", "price": 10}, # est
          "019": {"name": "Kwale", "price": 10}, # est
          "020": {"name": "Laikipia", "price": 50},
          "021": {"name": "Lamu", "price": 12}, # est
          "022": {"name": "Machakos", "price": 25},
          "023": {"name": "Makueni", "price": 10}, # est
          "024": {"name": "Mandera", "price": 10}, # est
          "025": {"name": "Marsabit", "price": 10}, # est
          "026": {"name": "Meru", "price": 15}, # est
          "027": {"name": "Migori", "price": 10}, # est
          "028": {"name": "Mombasa", "price": 10}, # est
          "029": {"name": "Murang'a", "price": 10}, # est
          "030": {"name": "Nairobi", "price": 50}, # est
          "031": {"name": "Nakuru", "price": 30}, 
          "032": {"name": "Nandi", "price": 10}, # est
          "033": {"name": "Narok", "price": 7}, # est
          "034": {"name": "Nyamira", "price": 10}, # est
          "035": {"name": "Nyandarua", "price": 15}, 
          "036": {"name": "Nyeri", "price": 7}, # est
          "037": {"name": "Samburu", "price": 10}, # est
          "038": {"name": "Siaya", "price": 30},
          "039": {"name": "Taita-Taveta", "price": 30},
          "040": {"name": "Tana River", "price": 10}, # est
          "041": {"name": "Tharaka-Nithi", "price": 10}, # est
          "042": {"name": "Trans-Nzoia", "price": 15}, # est
          "043": {"name": "Turkana", "price": 10}, # est
          "044": {"name": "Uasin Gishu", "price": 25},
          "045": {"name": "Vihiga", "price": 10}, # est
          "046": {"name": "Wajir", "price": 5},
          "047": {"name": "West Pokot", "price": 40},
          }
        for county_no, data in county_data.items():
            County.objects.create(county_no=int(county_no), county_name=data["name"], county_price=data["price"])
        