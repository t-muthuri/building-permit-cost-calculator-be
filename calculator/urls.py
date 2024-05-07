from django.urls import path
from . import views
urlpatterns = [
    path('counties-list/', views.county_list, name='counties'),
    path('project-type/', views.project_type, name='projects')
]
