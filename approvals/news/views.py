from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import HeadlineSerializer
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline


class HeadlineListView(generics.ListCreateAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer

class NewsScrapeView(APIView):
    def get(self, request, *args, **kwargs):
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://nation.africa/kenya"

        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class":"curation-module__item"})
        headlines = []
        for article in News:
            main = article.find_all('a')[0]
            link = main['href']
            title = main['title']
            headlines.append({'title': title, 'url': link})
            Headline.objects.update_or_create(title=title, url=link)
        
        return Response(headlines)
    
# class HeadlineListView(generics.ListCreateAPIView):
#     serializer_class = HeadlineSerializer

#     def get_queryset(self):
#         return Headline.objects.order_by('-id')[:10]