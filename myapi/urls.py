from django.urls import path
from . import views

urlpatterns = [
    path('crazy_enough/', views.crazy_enough, name='crazy_enough')
]