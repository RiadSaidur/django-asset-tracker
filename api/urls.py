from django.urls import path
from . import views

urlpatterns = [
  path('list-company/', views.ListCompany, name='list-company'),
  path('list-employee/', views.ListEmployee, name='list-employee'),
  path('list-asset/', views.ListAsset, name='list-asset'),
]
