from rest_framework import serializers
from .models import User, Member

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [ 'id', 'company_name', 'cac_reg_no', 'staff_pop', 'phone', 'email', 'address', 'is_company', 'is_hospital', 'password' ]
 
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address',  'password', 'entity']
