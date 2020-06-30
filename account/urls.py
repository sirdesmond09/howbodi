from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('company/', views.add_user),
    path('member/', views.add_member),
    path('member/upload', views.upload_member),
    path('auth/', views.logins),
    path('individuals/', views.individuals),
]