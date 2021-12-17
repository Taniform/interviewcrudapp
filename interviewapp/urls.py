from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
   path('project_details/<int:id>', project_details, name='project_details'),
   path('project_details/<int:id>', project_details, name='project_details'),
   path('building_details/<int:id>', building_details, name='building_details'),

]
