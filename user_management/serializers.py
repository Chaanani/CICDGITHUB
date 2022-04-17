from django.contrib.auth.models import User
from rest_framework import serializers

from user_management.models import TodoUserProfile


class TodoUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoUserProfile
        fields = ('phone', 'lucky_number')


class UserSerializer(serializers.ModelSerializer):

    profile = TodoUserProfileSerializer(source='todouserprofile')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile')
