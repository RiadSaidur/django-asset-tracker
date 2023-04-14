from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSeiralizer


@api_view(['GET'])
def ListEmployee(request):
  employees = Employee.objects.all()
  serializer = EmployeeSeiralizer(employees, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def AddEmployee(request):
  serializer = EmployeeSeiralizer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)

  return Response({ 'error': 'Employee add failed unexpectedy!' })