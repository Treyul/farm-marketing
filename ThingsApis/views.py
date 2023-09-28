from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from authentication import Thing_Auth


# Create your views here.
class Weather_Update_View(APIView):
    
    def post (self,request):
        authentication_classes = [Thing_Auth,]
        # get customer header define in the request 
        # UUID = request.M
        return

