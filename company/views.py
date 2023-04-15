from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySeiralizer


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def ListCompany(request):
  companies = Company.objects.all()
  serializer = CompanySeiralizer(companies, many=True)
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddComapany(request):
  serializer = CompanySeiralizer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)

  return Response({ 'error': 'Company add failed unexpectedy!' })