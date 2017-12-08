# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render_to_response,get_object_or_404

#from django.views.generic import ListView, DetailView

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from models import *

from serializers import *
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


class PlacesList(APIView):
    #show all
    def get(self,request):
        places1 = Places.objects.all()
        serializer = PlacesSerializer(places1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


class FloorsList(APIView):
    #show all
    def get(self,request):
        floors1 = Floors.objects.all()
        serializer = FloorsSerializer(floors1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


class DepartmentsList(APIView):
    #show all
    def get(self,request):
        departments1 = Departments.objects.all()
        serializer = DepartmentsSerializer(departments1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


class GeofencesList(APIView):
    #show all
    def get(self,request):
        geofences1 = Geofences.objects.all()
        serializer = GeofencesSerializer(geofences1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


class InputsList(APIView):
    #show all
    def get(self,request):
        inputs1 = Inputs.objects.all()
        serializer = InputsSerializer(inputs1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


class EventsList(APIView):
    #show all
    def get(self,request):
        events1 = Events.objects.all()
        serializer = Serializer(events1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass

def index (req):

    location = Location.objects.all()
    print (location)
    return render_to_response('index.html',{})
