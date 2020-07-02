from django.contrib import admin
from .models import User, Member, Individual

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'email', 'address', 'phone', 'is_hospital', 'is_company']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'entity', 'phone', 'company',]

class IndividualAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',  'phone', 'address', 'password',]

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Individual, IndividualAdmin)