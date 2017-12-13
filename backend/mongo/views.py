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

    def get_object(self, lat):
        try:
            return Location.objects.get(lat=lat)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, lat, format=None):
        location = self.get_object(lat)
        location = LocationSerializer(location)
        return Response(location.data)

    def put(self, request, lat, format=None):
        location = self.get_object(lat)
        serializer = LocationSerializer(location, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lat, format=None):
        location = self.get_object(lat)
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


class PlacesDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, id):
        try:
            return Places.objects.get(id=id)
        except Places.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        places = self.get_object(id)
        places = PlacesSerializer(places)
        return Response(places.data)

    def put(self, request, id, format=None):
        places = self.get_object(id)
        serializer = PlacesSerializer(places, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        places = self.get_object(id)
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

    def get_object(self, id):
        try:
            return Floors.objects.get(id=id)
        except Floors.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        floors = self.get_object(id)
        floors = FloorsSerializer(floors)
        return Response(floors.data)

    def put(self, request, id, format=None):
        floors = self.get_object(id)
        serializer = FloorsSerializer(floors, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        floors = self.get_object(id)
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

    def delete(self, request, id, format=None):
        return Response("ok")

class DepartmentsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, id):
        try:
            return Departments.objects.get(id=id)
        except Departments.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        departments = self.get_object(id)
        departments = DepartmentsSerializer(departments)
        return Response(departments.data)

    def put(self, request, id, format=None):
        departments = self.get_object(id)
        serializer = DepartmentsSerializer(departments, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        departments = self.get_object(id)
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

    def delete(self, request, id, format=None):
        return Response("ok")


class GeofencesDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, id):
        try:
            return Geofences.objects.get(id=id)
        except Geofences.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        geofences = self.get_object(id)
        geofences = GeofencesSerializer(geofences)
        return Response(geofences.data)

    def put(self, request, id, format=None):
        geofences = self.get_object(id)
        serializer = GeofencesSerializer(geofences, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        geofences = self.get_object(id)
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

    def delete(self, request, id, format=None):
        return Response("ok")

class InputsDetail(APIView):

    #Retrieve, update or delete a user instance.

    def get_object(self, id):
        try:
            return Inputs.objects.get(id=id)
        except Inputs.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        inputs = self.get_object(id)
        inputs = InputsSerializer(inputs)
        return Response(inputs.data)

    def put(self, request, id, format=None):
        inputs = self.get_object(id)
        serializer = InputsSerializer(inputs, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        inputs = self.get_object(id)
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

    def get_object(self, id):
        try:
            return Events.objects.get(id=id)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        events = self.get_object(id)
        events = EventsSerializer(events)
        return Response(events.data)

    def put(self, request, id, format=None):
        events = self.get_object(id)
        serializer = EventsSerializer(events, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        events = self.get_object(id)
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

    def delete(self, request, id, format=None):
        return Response("ok")


def index (req):

    location = Location.objects.all()
    print (location)
    return render_to_response('index.html',{})
