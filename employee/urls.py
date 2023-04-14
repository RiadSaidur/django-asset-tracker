from django.urls import path
from . import views

urlpatterns = [
  path('list-employee/', views.ListEmployee, name='list-employee'),
  path('add-employee/', views.AddEmployee, name='add-employee'),
]