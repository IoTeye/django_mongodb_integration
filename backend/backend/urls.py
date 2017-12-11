"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mongo.views import index
from mongo import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from mongoadmin import site

#admin.autodiscover()

urlpatterns = [
    #url(r'^admin/', site.urls),
    url(r'^admin/', admin.site.urls),
    #----test api
    url(r'^mongo/index/$',index),
    url(r'^core/Location/', views.LocationList.as_view()),
    #----get all information&&creat API
    url(r'^core/Places/', views.PlacesList.as_view()),
    url(r'^core/Floors/', views.FloorsList.as_view()),
    url(r'^core/Departments/', views.DepartmentsList.as_view()),
    url(r'^core/Geofences/', views.GeofencesList.as_view()),
    url(r'^core/Inputs/', views.InputsList.as_view()),
    url(r'^core/Events/', views.EventsList.as_view()),
    #----auth api
    url(r'^core_auth/login/', views.LoginList.as_view()),
    url(r'^core/current_user/', views.CurrentuserList.as_view()),
    #----delete API
    #----update API
    #----get a special API

]
