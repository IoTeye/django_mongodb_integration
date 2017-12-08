# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render_to_response,get_object_or_404

#from django.views.generic import ListView, DetailView

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from models import Location

from serializers import LocationSerializer
# Create your views here.

class LocationList(APIView):
    #show all
    def get(self,request):
        location1 = Location.objects.all()
        serializer = LocationSerializer(location1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass

def index (req):

    location = Location.objects.get()
    print location.lat
    return render_to_response('index.html',{})
