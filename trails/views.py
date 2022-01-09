from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import permission_required, login_required

from .models import trailModel, binocModel, displayData

#Display the trails from the trail model
class trailView(generic.ListView):
  model = trailModel
  template_name = 'trails/trails.html'
  context_object_name = 'trails'

  def get_queryset(self):
    return trailModel.getTrailData()
  
#Display the binoculars and their prices from the binoc model
class binocView(generic.ListView):
  model = binocModel
  template_name = 'trails/binocs.html'
  context_object_name = 'binocs'

  def get_queryset(self):
    return binocModel.getBinocData()

#Form to add a new trail. Decorators to require permissions to add trails
@login_required
@permission_required('trails.add_trailmodel')
def addTrail(request):
  return render(request, 'trails/addTrail.html')
 
#Add a new trail and render the new list. Decorators to require permissions to add trails
@login_required
@permission_required('trails.add_trailmodel')
def newTrail(request):
  newTrailList = trailModel.getTrailData() #Get initial trail list
  newTrailList.append(request.GET['trail']) #Append the new trail from the user
  return render(request, 'trails/newTrails.html', {'newTrail': newTrailList})

#Form to remove a trail from the list. Decorators to require permission to remove trails.
@login_required
@permission_required('trails.delete_trailmodel')
def removeTrail(request):
  return render(request, 'trails/removeTrail.html')

#Remove the trail from the list and display a new page with the updated list. Decorators to require permission to remove trails.
@login_required
@permission_required('trails.delete_trailmodel')
def displayRemovedTrail(request):
  removeList = trailModel.getTrailData() #Get the initial trail list
  if(request.GET['trail'] in removeList): #If the trail is in the list, remove it
    removeList.remove(request.GET['trail'])
    return render(request, 'trails/removedTrails.html', {'removeTrail': removeList})
  return render(request, 'trails/notRemovedTrails.html', {'newTrail': removeList})

#Display the graph from the graph model
def displayGraph(request):
   return render(request, 'trails/visual.html', context={'plot_div': displayData.getBinocPrices()})

#Display the default home view
def defaultView(request):
  return render(request, 'trails/home.html')

#Display information page
def displayInfo(request):
  return render(request, 'trails/information.html')