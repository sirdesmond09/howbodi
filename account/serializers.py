from rest_framework import serializers
from .models import UserTable
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = UserTable
        fields = ['firstname', 'lastname', 'email', 'password', 'is_super_admin', 'is_admin', 'is_user']
        