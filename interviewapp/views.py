from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# import boto3

from .models import *


def landing(request):

    get_projects = Project.objects.all()

    project = Project()
    if request.POST:
        project.project_name = request.POST["project_name"] 
        
        project.save()


    template = "landing.html"
    context = {
      "get_projects":get_projects
    }
    return render(request, template, context)


def project_details(request, id):
    get_project = Project.objects.get(id = id)
    get_buildings = Building.objects.all()
    
    building = Building()

    if request.POST:
        building.bulding_name = request.POST["bulding_name"] 
        building.bulding_type = request.POST["bulding_type"] 

        building.project = get_project
        
        building.save()


    template = "project_details.html"
    context = {
      "get_project":get_project,
      "get_buildings":get_buildings,
    }
    return render(request, template, context)


def building_details(request, id):
    get_building = Building.objects.get(id = id)
    get_appartments = Appartment.objects.all()
    
    appartment = Appartment()

    if request.POST:
        appartment.number_of_rooms = request.POST["number_of_rooms"] 
        appartment.floor_number = request.POST["floor_number"] 

        appartment.building = get_building
        
        appartment.save()


    template = "building_details.html"
    context = {
      "get_building":get_building,
      "get_appartments":get_appartments,
    }
    return render(request, template, context)