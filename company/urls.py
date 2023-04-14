from django.urls import path
from . import views

urlpatterns = [
  path('list-company/', views.ListCompany, name='list-company'),
]