from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Member
from .serializers import UserSerializer, MemberSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def add_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many =True)
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid():

            user = User.objects.create_user(**serializer.validated_data)
            token = Token.objects.create(user = user)
            # t = Token.objects.get(user=user)
            # user.token = t.key
            user.save()

            serializer = UserSerializer(user)
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Sign up successful",
                'data' : serializer.data,
            }

            return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : status.HTTP_400_BAD_REQUEST,
                'message' : "Unsuccessful",
                'data' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def add_member(request):
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many =True)
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        
        serializer = MemberSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password']) #hash the given password                
            member = Member.objects.create(**serializer.validated_data)
            member.save()

            serializer = MemberSerializer(member)
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Sign up successful",
                'data' : serializer.data,
            }

            return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : status.HTTP_400_BAD_REQUEST,
                'message' : "Unsuccessful",
                'data' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def upload_member(request):

    if request.method == 'POST':
        
        serializer = MemberSerializer(data = request.data, many =True)
        
        if serializer.is_valid():
     

                for i in serializer.validated_data:
                    
                    member = Member.objects.create(**i)
                    member.save()

                
                data = {
                    'status'  : status.HTTP_201_CREATED,
                    'message' : "Upload successful",
                    'data' : serializer.data,
                }

                return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : status.HTTP_400_BAD_REQUEST,
                'message' : "Unsuccessful",
                'data' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)



@api_view([ 'POST'])
def logins(request):
    
    if request.method == "POST":
        
        user = authenticate(request, email = request.data['email'], password = request.data['password'])
        if user is not None:
            try:
                company = User.objects.get(email = user.email)
                serializer = UserSerializer(company)

                data = {
                    'status'  : status.HTTP_202_ACCEPTED,
                    'message' : "Authenticated successfully",
                    'data' : serializer.data,
                }

                return Response(data, status=status.HTTP_202_ACCEPTED)
            
            except User.DoesNotExist:

                member = Member.objects.get(email = user.email)
                serializer = MemberSerializer(member)

                data = {
                    'status'  : status.HTTP_202_ACCEPTED,
                    'message' : "Authenticated successfully",
                    'data' : serializer.data,
                }

                return Response(data, status=status.HTTP_202_ACCEPTED)

                

                

        else:
            data = {
                    'status'  : status.HTTP_401_UNAUTHORIZED,
                    'message' : "Unsuccessful",
                    'data' : request.data,
                }
            return Response(data)


@api_view(['GET', 'POST'])
def individuals(request):
    if request.method == 'GET':
        user = User.objects.get(is_individual = True)
        try:
            member = Member.objects.get_queryset().filter(entity = user)
            
            serializer = MemberSerializer(member, many =True)
            data = {
                    'status'  : status.HTTP_200_OK,
                    'message' : "Successful",
                    'data' : serializer.data,
                }

            return Response(data, status=status.HTTP_200_OK)
            
        except Member.DoesNotExist:
            data = {
                    'status'  : status.HTTP_404_NOT_FOUND,
                    'message' : "Unsuccessful",
                    'data' : "Individuals does not exist",
                }

            return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        
        serializer = MemberSerializer(data = request.data)
        
        if serializer.is_valid():
            if not serializer.data['entity']:
                user = User.objects.get(is_individual =True)
                serializer.validated_data['entity'] = user
                serializer.validated_data['password'] = make_password(serializer.validated_data['password']) #hash the given password
                member = Member.objects.create(**serializer.validated_data)
                member.save()

                serializer = MemberSerializer(member)
                data = {
                    'status'  : status.HTTP_201_CREATED,
                    'message' : "Sign up successful",
                    'data' : serializer.data,
                }

                return Response(data, status = status.HTTP_201_CREATED)

        else:
            data = {
                'status'  : status.HTTP_400_BAD_REQUEST,
                'message' : "Unsuccessful",
                'data' : serializer.errors,
            }

            return Response(data, status = status.HTTP_400_BAD_REQUEST)