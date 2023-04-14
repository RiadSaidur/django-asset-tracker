from django.urls import path
from . import views

urlpatterns = [
  path('list-asset/', views.ListAsset, name='list-asset'),
  path('list-employee-asset/<int:id>', views.ListAssetByEmployee, name='list-asset-by-employee'),
  path('list-company-asset/<int:id>', views.ListAssetByCompany, name='list-asset-by-company'),
  path('add-asset/', views.AddAsset, name='add-asset'),
]