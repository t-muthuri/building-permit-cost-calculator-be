from django.urls import path
# from . import views
from .views import HeadlineListView, NewsScrapeView

urlpatterns = [
    path('headlines/', HeadlineListView.as_view(), name='headline-list'),
    path('scrape-news/', NewsScrapeView.as_view(), name='news-scrape'),
]