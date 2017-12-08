# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Places,Floors,Departments,Geofences,Inputs,Events
# Register your models here.

admin.site.register(Places)
admin.site.register(Floors)
admin.site.register(Departments)
admin.site.register(Geofences)
admin.site.register(Inputs)
admin.site.register(Events)

'''
from mongoadmin import site, DocumentAdmin
class AppDocumentAdmin(DocumentAdmin):
    pass
site.register(Places,PlacesAdmin)
site.register(Floors,FloorsAdmin)
site.register(Departments,DepartmentsAdmin)
site.register(Geofences,GeofencesAdmin)
site.register(Inputs,InputsAdmin)
site.register(Events,EventsAdmin)
'''
