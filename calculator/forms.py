from django import forms

# # PROJECT_CHOICES = {
# #     "Residential": "Residential",
# #     "Institutional": "Institutional",
# #     "Mixed Use Building": "Mixed Use Building",
# #     "Office": "Office",
# #     "Hospitality": "Hospitality"
# # }

# # COUNTY_CHOICES = {
# #     "1": "Mombasa",
# #     "2": "Kwale",
# #     "3": "Kilifi",
# #     "4": "Tana River",
# #     "5": "Lamu",
# #     "6": "Taita-Taveta",
# #     "7": "Garissa",
# #     "8": "Wajir",
# #     "9": "Mandera",
# #     "10": "Marsabit",
# #     }

class CalculatorForm(forms.Form):
    # instance variables mapping the labels
    project_size = forms.FloatField(label="The size of your project")
    type_of_project = forms.CharField(label="Type of project")
    county = forms.CharField(label="County")
    total_cost_of_construction_project = forms.FloatField()