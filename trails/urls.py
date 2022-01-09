from django.urls import path, include
from . import views

app_name = 'trails'

#URLS for django page
urlpatterns = [
  path('', views.defaultView, name='default'), #Default view
  path('trails/', views.trailView.as_view(), name='trails'), #List of trails
  path('addTrail/', views.addTrail, name='addTrail'), #Form to add a trail
  path('newTrails/', views.newTrail, name='newTrail'), #List with new trail
  path('removeTrail/', views.removeTrail, name='removeTrail'), #Remove trails
  path('removedTrails/', views.displayRemovedTrail, name='removedTrails'), #See removed trails
  path('binocs/', views.binocView.as_view(), name='binoculars'), #List of binocs
  path('graph/', views.displayGraph, name='graph'), #Graph of prices
  path('information/', views.displayInfo, name ='information'), #Display information page
  path('accounts/', include('django.contrib.auth.urls')), #Account login page
]