from django.urls import path
from . import views
urlpatterns = [
    path('calculator/', views.county_list, name='county_list'),
]
