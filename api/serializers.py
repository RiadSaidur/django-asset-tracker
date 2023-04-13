from rest_framework import serializers
from .models import Company, Employee, Asset

class CompanySeiralizer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'


class EmployeeSeiralizer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'


class AssetSeiralizer(serializers.ModelSerializer):
  class Meta:
    model = Asset
    fields = '__all__'