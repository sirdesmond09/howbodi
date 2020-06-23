from django.contrib import admin
from .models import UserTable

class UserTableAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'is_super_admin', 'is_admin', 'is_user']

admin.site.register(UserTable, UserTableAdmin)