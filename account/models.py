from django.db import models
from django.contrib.auth.models import User

class UserTable(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname      = models.CharField(max_length = 250)
    lastname       = models.CharField(max_length = 250)
    email          = models.EmailField(max_length = 250)
    password       = models.CharField(max_length = 250)
    is_super_admin = models.BooleanField(blank=True)
    is_admin       = models.BooleanField(blank=True)
    is_user        = models.BooleanField(blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}' 

