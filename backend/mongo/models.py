# -*- coding: utf-8 -*-
from django.db import models

from djangotoolbox.fields import ListField,DictField,EmbeddedModelField
# Create your models here.
places = ListField(EmbeddedModelField('Places'))

class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    zoom = models.IntegerField()

class Places(models.Model):
    address = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    location = EmbeddedModelField('Location')
    name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = CharField(max_length=200)
    tags = ListField()
    updatedAt = models.DateTimeField(auto_now_add=True)
    geopoint = ListField()


class Floors(models.Model):
    anchors = ListField()
    createdAt = models.DateTimeField(auto_now_add=True)
    floorplan_image_url = models.URLField¶()
    indooratlas_floor_id =models.CharField(max_length=36)
    indooratlas_floorplan_id = models.CharField(max_length=36)
    name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    organization_name = CharField(max_length=200)
    place_id = models.IntegerField()
    updatedAt = models.DateTimeField(auto_now_add=True)
    geopoint = ListField()

class departments(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    floor_id = models.CharField(max_length=36)
    floor_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    organization_id = models.IntegerField()
    organization_name = CharField(max_length=200)
    place_id = models.CharField(max_length=36)
    place_name = models.CharField(max_length=100)
    tags = ListField()
    updatedAt = models.DateTimeField(auto_now_add=True)


class Area(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()


class Geofences(models.Model):
    area = EmbeddedModelField('Area')
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=36)
    address = models.TextField()
    department_id = models.IntegerField()
    radius = models.CharField()
    organization_id = models.CharField(max_length=36)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    organization_name = CharField(max_length=200)
    place_name = models.CharField(max_length=100)
    geopoint = ListField()




class Inputs(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    "data": {
        "instanceid": null,
        "major": 1,
        "marker": {
        "lat": 40.6620232,
        "lng": -74.6283752
        },
        "minor": 1,
        "namespaceid": null,
        "uuid": "1"
        },
    department_id = models.CharField(max_length=36)
    floor_id = models.CharField(max_length=36)
    name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)
    place_id = models.CharField(max_length=36)
    type = models.CharField(max_length=100)
    geopoint = ListField()
    updatedAt = models.DateTimeField(auto_now_add=True)

class Events(models.Model):
    event = models.CharField(max_length=100)
    data = EmbeddedModelField('Data')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)


class Data(models.Model):
    operation = models.CharField(max_length=100)
    target = models.CharField(max_length=36)
    type = models.CharField(max_length=36)
    tags = ListField()
