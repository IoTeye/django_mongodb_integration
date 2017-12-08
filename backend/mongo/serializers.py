from rest_framework import serializers
from models import Location

class LocationSerializer(serializers.Serializer):

    class Meta:
        models=Location
        fields=('lat','lng','zoom')
        #fields='__all__'
