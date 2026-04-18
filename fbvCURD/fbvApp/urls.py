from django.urls import path
from .views import getStudents,createStudent,home,deleteStudent,updateStudent,logoutUser

urlpatterns = [
    path("",home),
    path('list/',getStudents),
    path('create/',createStudent),
    path('delete/<int:id>/',deleteStudent),
    path('update/<int:id>/',updateStudent),
    path('logout/',logoutUser)
]