from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [

    #company users
    path('company/', views.add_company),
    path('company/<int:pk>', views.company_detail),

    #members of company or patients of hospital
    path('member/', views.add_member),
    path('member/upload', views.upload_member),
    path('member/<int:pk>', views.member_detail),

    #company and member login
    path('auth/', views.logins),


    #individual users
    path('individuals/', views.individuals),
    path('individuals/login', views.individual_login),
    path('individuals/<int:pk>', views.individual_detail),
]