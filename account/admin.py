from django.contrib import admin
from .models import User, Member

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'email', 'address', 'phone', 'is_hospital', 'is_company']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'entity', 'phone', 'address',]

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)