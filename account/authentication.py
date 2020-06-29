"""
My custom authentication
Authenticate using an e-mail address.
"""
from .models import User, Member

class CustomUserAuthBackend(object):

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        
            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, member_id):
        try:
            return User.objects.get(pk=member_id)
        except User.DoesNotExist:
            return None

class CustomMemberAuthBackend(object):
    
    def authenticate(self, request, email=None, password=None):
        try:
            member = Member.objects.get(email=email)
            if member.check_password(password):
                return member
        
            return None
        except Member.DoesNotExist:
            return None
    
    def get_member(self, member_id):
        try:
            return Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return None