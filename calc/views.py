from django.shortcuts import render
# import the generic view class that gives access to the CRUD functions
from django.views import View
from .forms import  CalcForm

# Create your views here.
class Index(View):
    def get(self, request):
        form = CalcForm() # render an empty form
        return render(request, 'calc/index.html', {'form': form})

    def post(self, request):
        form = CalcForm(request.POST) # user input

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

        # render the template
        return render(request, 'calc/result.html', context)