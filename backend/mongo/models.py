# -*- coding: utf-8 -*-
from django.db import models

from djangotoolbox.fields import ListField,DictField,EmbeddedModelField
# Create your models here.


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
    organization_name = models.CharField(max_length=200)
    tags = ListField()
    updatedAt = models.DateTimeField(auto_now_add=True)
    geopoint = ListField()

class Anchor(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()




class Floors(models.Model):
    anchors = ListField(DictField())
    createdAt = models.DateTimeField(auto_now_add=True)
    floorplan_image_url = models.URLField(blank=True)
    indooratlas_floor_id =models.CharField(max_length=36,blank=True)
    indooratlas_floorplan_id = models.CharField(max_length=36,blank=True)
    name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)
    place_id = models.CharField(max_length=36)
    updatedAt = models.DateTimeField(auto_now_add=True)
    geopoint = ListField()

class Departments(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    floor_id = models.CharField(max_length=36)
    floor_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)
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
    department_id = models.CharField(max_length=36,null=True,blank=True)
    radius = models.FloatField()
    organization_id = models.CharField(max_length=36)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    organization_name = models.CharField(max_length=200)
    place_name = models.CharField(max_length=100)
    geopoint = ListField()

class Marker(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

class Data(models.Model):
    instanceid = models.CharField(max_length=36,blank=True)
    major = models.IntegerField(blank=True)
    minor = models.IntegerField(blank=True)
    namespaceid = models.CharField(max_length=36,blank=True)
    uuid = models.CharField(max_length=36,blank=True)
    marker = EmbeddedModelField('Marker',blank=True)
    operation = models.CharField(max_length=100,blank=True)
    target = models.CharField(max_length=36,blank=True)
    type = models.CharField(max_length=36,blank=True)
    tags = ListField(null=True,blank=True)
    id = models.CharField(max_length=36,primary_key=True,blank=True)
    email = models.EmailField(max_length=254,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True,blank=True)
    name = models.CharField(max_length=100,blank=True)
    organization_id = models.CharField(max_length=36,blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True,blank=True)
    password = models.TextField(blank=True)
    token = models.TextField(blank=True)

class Inputs(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    data = EmbeddedModelField('Data')
    department_id = models.CharField(max_length=36)
    floor_id = models.CharField(max_length=36,blank=True)
    name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)
    place_id = models.CharField(max_length=36,blank=True)
    type = models.CharField(max_length=100)
    geopoint = ListField(blank=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Events(models.Model):
    event = models.CharField(max_length=100)
    data = EmbeddedModelField('Data')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)


class User(models.Model):
    id = models.CharField(max_length=36,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


class Red(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    expiresAt = models.DateTimeField()
    host = models.CharField(max_length=16)
    port = models.IntegerField()
    shared = models.BooleanField()

class Organization(models.Model):
    id = models.CharField(max_length=36,primary_key=True)
    name = models.CharField(max_length=200)
    background = models.CharField(max_length=100)
    country = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    stripe = models.BooleanField()
    plan = models.CharField(max_length=36)
    planStatus = models.CharField(max_length=36)
    trialEnd = models.IntegerField()
    eventBusToken = models.TextField()
    positionsToken = models.TextField()
    proximiioBusToken = models.TextField()
    proximiioBusRef = models.URLField()
    eventBusRef = models.URLField()
    red = EmbeddedModelField('Red')

class Settings(models.Model):
    eddystone = models.BooleanField()
    gpsgeofences = models.BooleanField()
    ibeacons = models.BooleanField()
    indooratlas = models.BooleanField()
    indooratlasapikey = models.CharField(max_length=200)
    indooratlasapikeysecret = models.CharField(max_length=200)
    steerpath = models.BooleanField()
    steerpathndd = models.CharField(max_length=200)

class Application(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=36,primary_key=True)
    name = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=36)
    organization_name = models.CharField(max_length=200)
    settings = EmbeddedModelField('Settings')
    type = models.CharField(max_length=20)
    updatedAt = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    user = EmbeddedModelField('User')
    token = models.TextField()
    organization = EmbeddedModelField('Organization')
    application = EmbeddedModelField('Application')

class Tokens(models.Model):
    type = models.CharField(max_length=20)
    user = models.CharField(max_length=100)
    user_id = models.CharField(max_length=36)
    tenant_id = models.CharField(max_length=36)
    application_id = models.CharField(max_length=36)

class Current_user(models.Model):
    id = models.CharField(max_length=36,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    organization_id = models.CharField(max_length=36)
    organization = EmbeddedModelField('Organization')
    tokens = ListField(DictField())
    data = EmbeddedModelField('Data')
    type = models.CharField(max_length=20)
