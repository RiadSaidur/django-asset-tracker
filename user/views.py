from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['POST'])
def register(request):
  if not request.data.company_name:
    return Response({ 'error': 'Comapny Name required!' })
  
  serializer = UserSerializer(data=request.data)
  
  if serializer.is_valid():
    serializer.save()
    return Response({ 'success': 'User successfully created.' })
  
  return Response({ 'error': 'Registration failed unexpectedy!' })

