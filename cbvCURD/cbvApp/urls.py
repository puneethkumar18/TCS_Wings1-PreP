from django.urls import path
from  .views import StudentListView,StudentDetailView,StudentCreateView,StudentDeleteView,StudentUpdateView


urlpatterns = [
    path('students/',StudentListView.as_view(),name='students'),
    path('<int:pk>/',StudentDetailView.as_view(),name="details"),
    path('create/',StudentCreateView.as_view()),
    path('update/<int:pk>',StudentUpdateView.as_view()),
    path('delete/<int:pk>/',StudentDeleteView.as_view()),

]
