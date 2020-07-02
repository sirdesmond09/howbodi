"""
My custom authentication
Authenticate using an e-mail address.
"""
from .models import User, Member, Individual

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

class CustomIndividualAuthBackend(object):
    
    def authenticate(self, request, email=None, password=None):
        try:
            individual = Individual.objects.get(email=email)
            if individual.check_password(password):
                return individual
        
            return None
        except Individual.DoesNotExist:
            return None
    
    def get_individual(self, individual_id):
        try:
            return Individual.objects.get(pk=individual_id)
        except Individual.DoesNotExist:
            return None