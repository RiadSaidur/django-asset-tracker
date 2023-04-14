from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySeiralizer


@api_view(['GET'])
def ListCompany(request):
  companies = Company.objects.all()
  serializer = CompanySeiralizer(companies, many=True)
  return Response(serializer.data)

