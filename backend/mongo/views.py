# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView

from models import *
# Create your views here.
def index (req):

    location = Location.objects.get()
    print location.lat
    return render_to_response('index.html',{})
