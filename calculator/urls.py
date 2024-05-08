from django.urls import path
from . import views

urlpatterns = [
    path('counties-list/', views.county_list, name='counties'),
    path('project-types-list/', views.project_type_list, name='project_types')
]
