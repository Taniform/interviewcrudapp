from django.db import models
from django.db.models import Q, Avg, Sum

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True)

    timestamp = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return str(self.project_name)


class Building(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    bulding_name = models.CharField(max_length=255, unique=True)
    bulding_type = models.CharField(max_length=255, unique=True)

    timestamp = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return str(self.bulding_name)
	


class Appartment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number_of_rooms = models.CharField(max_length=255, unique=True)
    floor_number = models.CharField(max_length=255, unique=True)

    timestamp = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return str(self.building.bulding_name)