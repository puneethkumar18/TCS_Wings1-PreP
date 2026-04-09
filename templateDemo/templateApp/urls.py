from django.urls import path
from .views import welcome,renderData,elctronics
urlpatterns = [
    path('',welcome),
    path("electronics/",elctronics,name="electronics"),
    path('welcome/',welcome,name='welcome'),
    path('home/',renderData,name='renderdata'),
]
