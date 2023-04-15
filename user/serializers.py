from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'password', 'email')

  def create(self, data):
    user = User.objects.create(
      username=data['username'],
      email=data['email'],
    )

    
    user.set_password(data['password'])
    user.save()

    return user