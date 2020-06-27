from rest_framework import serializers
from .models import User, Member

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [ 'id', 'company_name', 'phone', 'email', 'address', 'is_company', 'is_hospital',  'token']
 
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address',  'password', 'entity']
