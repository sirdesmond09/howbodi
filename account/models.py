from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.hashers import check_password

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    company_name  = models.CharField(_('company name'),max_length = 250)
    cac_reg_no    = models.CharField(_('Registration number'), max_length=50)
    email         = models.EmailField(_('email'), unique=True)
    phone         = models.CharField(_('phone'), max_length = 20, null = True)
    address       = models.CharField(_('address'), max_length = 250, null = True)
    state         = models.CharField(_('state'), max_length = 250, null = True)
    local_gov     = models.CharField(_('local government'), max_length = 250, null = True)
    industry      = models.CharField(_('industry'), max_length = 250, null = True)
    staff_pop     = models.IntegerField(_('staff population'))
    password      = models.CharField(_('password'), max_length=300)
    is_staff      = models.BooleanField(_('staff'), default=False)
    is_company    = models.BooleanField(_('company'), default=False)
    is_hospital   = models.BooleanField(_('hospital'), default=False)
    is_superuser  = models.BooleanField(_('super user'), default=False)
    is_active     = models.BooleanField(_('active'), default=True)
    date_joined   = models.DateTimeField(_('date joined'), auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.company_name



class Member(models.Model):
    entity           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,serialize = True, null = True)
    first_name       = models.CharField(max_length=30)
    last_name        = models.CharField(max_length=30)
    email            = models.EmailField(unique = True)
    phone            = models.CharField(max_length = 20)
    company          = models.CharField(max_length = 150, blank = True)
    assessment_taken = models.IntegerField(default = 0)
    password         = models.CharField(blank=True, max_length=300)
    date_joined      = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.email
    
    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)# Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)


class Individual(models.Model):
    first_name       = models.CharField(max_length=30)
    last_name        = models.CharField(max_length=30)
    email            = models.EmailField(unique = True)
    phone            = models.CharField(max_length = 20)
    address          = models.CharField(max_length = 250)    
    assessment_taken = models.IntegerField(default = 0)
    password         = models.CharField(max_length=300)
    date_joined      = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.email
    
    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)# Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)