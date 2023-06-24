import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
import requests

from .serializers import movie_serializer
from django.core import serializers
# Create your views here.

class title(APIView):
    def get(self,request):
        title = request.GET.get('title')
        APIKEY = 'a956febd'
        url = f'https://www.omdbapi.com/?i=tt3896198&apikey={APIKEY}&t={title}'
        
        response = requests.get(url)
        content = response.content

        # Get the raw content from the response
        content = response.content

        # Convert the content to a Python dictionary using json.loads()
        data = json.loads(content)

        # Create a JsonResponse object using the serialized_data
        json_response = JsonResponse(data, safe=False)
        return json_response

