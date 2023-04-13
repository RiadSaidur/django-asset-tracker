from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Company, Employee, Asset
from .serializers import CompanySeiralizer, EmployeeSeiralizer, AssetSeiralizer

@api_view(['GET'])
def ListCompany(request):
  companies = Company.objects.all()
  serializer = CompanySeiralizer(companies, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def ListEmployee(request):
  employees = Employee.objects.all()
  serializer = EmployeeSeiralizer(employees, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def ListAsset(request):
  assets = Asset.objects.all()
  serializer = AssetSeiralizer(assets, many=True)
  return Response(serializer.data)