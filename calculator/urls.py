from django.urls import path
from . import views
urlpatterns = [
    path('calculator/', views.calculator, name='calculator'),
    path('counties-list/', views.county_list, name='counties'),
]
