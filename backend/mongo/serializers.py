from rest_framework import serializers
from models import *

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields=('lat','lng','zoom')
        #fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Places
        fields=('address','createdAt','location','name','organization_id','organization_name','tags','updatedAt','geopoint')
        #fields = '__all__'

class FloorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Floors
        fields=('anchors','createdAt','floorplan_image_url','indooratlas_floor_id','indooratlas_floorplan_id','name','place_name','rganization_id','organization_name','place_id','updatedAt','geopoint')
        #fields = '__all__'

class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields=('createdAt','floor_id','floor_name','name','organization_id','organization_name','place_id','place_name','tags','updatedAt')
        #fields = '__all__'


class GeofencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geofences
        fields=('area','name','place_id','address','department_id','radius','organization_id','createdAt','updatedAt','organization_name','place_name','geopoint')
        #fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields=('event','data','createdAt','updatedAt','organization_id','organization_name')
        #fields = '__all__'

class InputsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inputs
        fields=('createdAt','data','department_id','floor_id','name','organization_id','organization_name','place_id','type','geopoint','updatedAt')
        #fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields=('user','token','organization','application')

class CurrentuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Current_user
        fields=('id','name','email','organization_id','organization','tokens','data','type')
