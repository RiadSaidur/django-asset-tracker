from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Asset
from .serializers import AssetSeiralizer


@api_view(['GET'])
def ListAsset(request):
  assets = Asset.objects.all()
  serializer = AssetSeiralizer(assets, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def ListAssetByEmployee(request, id):
  assets = Asset.objects.filter(employee=id)
  serializer = AssetSeiralizer(assets, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def ListAssetByCompany(request, id):
  assets = Asset.objects.filter(employee__company=id)
  serializer = AssetSeiralizer(assets, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def AddAsset(request):
  serializer = AssetSeiralizer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)

  return Response({ 'error': 'Asset add failed unexpectedy!' })