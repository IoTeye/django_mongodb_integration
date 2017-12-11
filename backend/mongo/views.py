# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render_to_response,get_object_or_404

#from django.views.generic import ListView, DetailView

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from django.http import Http404

from models import *

from serializers import *
# Create your views here.

class LocationList(APIView):
    #permission_classes = (permissions.AllowAny,)
    #show all
    def get(self,request,format=None):
        print request.method

        location1 = Location.objects.all()
        serializer = LocationSerializer(location1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = LocationSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")

class PlacesList(APIView):
    #show all
    def get(self,request):
        places1 = Places.objects.all()
        serializer = PlacesSerializer(places1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = PlacesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


class FloorsList(APIView):
    #show all
    def get(self,request):
        floors1 = Floors.objects.all()
        serializer = FloorsSerializer(floors1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = FloorsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


class DepartmentsList(APIView):
    #show all
    def get(self,request):
        departments1 = Departments.objects.all()
        serializer = DepartmentsSerializer(departments1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = DepartmentsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


class GeofencesList(APIView):
    #show all
    def get(self,request):
        geofences1 = Geofences.objects.all()
        serializer = GeofencesSerializer(geofences1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = GeofencesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


class InputsList(APIView):
    #show all
    def get(self,request):
        inputs1 = Inputs.objects.all()
        serializer = InputsSerializer(inputs1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = InputsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


class EventsList(APIView):
    #show all
    def get(self,request):
        events1 = Events.objects.all()
        serializer = EventsSerializer(events1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = EventsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")

class LoginList(APIView):
    #show all
    def get(self,request):
        account1 = Account.objects.all()
        serializer = LoginSerializer(account1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass

class CurrentuserList(APIView):
    #show all
    def get(self,request):
        Currentuser1 = Current_user.objects.all()
        serializer = CurrentuserSerializer(Currentuser1,many=True)
        print(serializer)
        return Response(serializer.data)

    #add one
    def post(self):
        pass


def index (req):

    location = Location.objects.all()
    print (location)
    return render_to_response('index.html',{})
