from django.urls import path
from .views import addProject,index,listOfProjects

urlpatterns = [
   path('',index),
   path('add-project/',addProject),
   path('list/',listOfProjects)
]
