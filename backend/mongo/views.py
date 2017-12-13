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
    #List all users, or create a new user.
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


class LocationDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
    except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        location = LocationSerializer(location)
        return Response(location.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




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

class PlacesDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Places.objects.get(pk=pk)
    except Places.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        places = self.get_object(pk)
        places = PlacesSerializer(places)
        return Response(places.data)

    def put(self, request, pk, format=None):
        places = self.get_object(pk)
        serializer = PlacesSerializer(places, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        places = self.get_object(pk)
        places.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class FloorsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Floors.objects.get(pk=pk)
    except Floors.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        floors = self.get_object(pk)
        floors = FloorsSerializer(floors)
        return Response(floors.data)

    def put(self, request, pk, format=None):
        floors = self.get_object(pk)
        serializer = FloorsSerializer(floors, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        floors = self.get_object(pk)
        floors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class DepartmentsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Departments.objects.get(pk=pk)
    except Departments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        departments = self.get_object(pk)
        departments = DepartmentsSerializer(departments)
        return Response(departments.data)

    def put(self, request, pk, format=None):
        departments = self.get_object(pk)
        serializer = DepartmentsSerializer(departments, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        departments = self.get_object(pk)
        departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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


class GeofencesDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Geofences.objects.get(pk=pk)
    except Geofences.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        geofences = self.get_object(pk)
        geofences = GeofencesSerializer(geofences)
        return Response(geofences.data)

    def put(self, request, pk, format=None):
        geofences = self.get_object(pk)
        serializer = GeofencesSerializer(geofences, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        geofences = self.get_object(pk)
        geofences.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class InputsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Inputs.objects.get(pk=pk)
    except Inputs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inputs = self.get_object(pk)
        inputs = InputsSerializer(inputs)
        return Response(inputs.data)

    def put(self, request, pk, format=None):
        inputs = self.get_object(pk)
        serializer = InputsSerializer(inputs, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inputs = self.get_object(pk)
        inputs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class EventsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, pk):
        try:
            return Events.objects.get(pk=pk)
    except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk)
        events = EventsSerializer(events)
        return Response(events.data)

    def put(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventsSerializer(events, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        a={"id": "0991202f-521b-450b-981f-14beac2c1ca1","name": "Sheng Ming-Jye","email": "mingjye.sheng@ioteyeinc.com","organization_id": "3b8ae3c0-3527-431b-a444-8e62c4da077e","organization": {"id": "3b8ae3c0-3527-431b-a444-8e62c4da077e","name": "Ming-Jye Sheng","background": "United States","country": "United States","email": "mingjye.sheng@ioteyeinc.com","plan": "guru","planStatus": "trialing","trialEnd": 1506966163,"proximiioBusRef": "https://proximiio-bus.firebaseio.com/organizations/3b8ae3c0-3527-431b-a444-8e62c4da077e","eventBusRef": "https://proximiio-event-bus.firebaseio.com/organizations/3b8ae3c0-3527-431b-a444-8e62c4da077e"}
}
        #return Response(serializer.data)
        return Response(a)
    #add one
    def post(self,request,format=None):
        print request.DATA
        serializer = CurrentuserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response("ok")


def index (req):

    location = Location.objects.all()
    print (location)
    return render_to_response('index.html',{})
