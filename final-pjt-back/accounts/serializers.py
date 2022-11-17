from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField()
    class Meta:
        model = User
        fields = ('username',)