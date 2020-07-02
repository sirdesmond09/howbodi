from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Member, Individual
from .serializers import UserSerializer, MemberSerializer, IndividualSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def add_company(request):
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




###MEMBERS OF ORGANIZATIONS AND HOSPITALS

#Add single member
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
            
            company = User.objects.get(company_name =serializer.validated_data['entity'])              
            serializer.validated_data['company'] = company.company_name   
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


#Upload list of members

@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def upload_member(request):

    if request.method == 'POST':
        
        serializer = MemberSerializer(data = request.data, many =True)
        
        if serializer.is_valid():
     

                for i in serializer.validated_data:
                    company = User.objects.get(company_name =i['entity'])              
                    i['company'] = company.company_name
                    
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


#Login as a member or an organization
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



#Get the detail of a single organization or hospital by their ID
@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def company_detail(request, pk):
    try:
        company = User.objects.get(pk = pk)
    
    except User.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(company)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    #Update the profile of the organization
    elif request.method == 'PUT':
        serializer = UserSerializer(company, data = request.data, partial=True) #allows you to be able to update one field of the model

        if serializer.is_valid():
            
            #check if it's password change and hash the new password
            if "password" in serializer.validated_data.keys():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        
            serializer.save()

            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated profile",
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

    #delete the account
    elif request.method == 'DELETE':
        company.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


#Get the detail of a single member by their ID

@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def member_detail(request, pk):
    try:
        member = Member.objects.get(pk = pk)
    
    except Member.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    #Update the profile of the individual
    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data = request.data, partial=True) #allows you to be able to update one field of the model

        if serializer.is_valid():
            
            #check if it's password change and hash the new password
            if "password" in serializer.validated_data.keys():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        
            serializer.save()

            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated profile",
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

    #delete the account
    elif request.method == 'DELETE':
        member.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)





                        #####INDIVIDUAL USERS###

#Individual user signup and view all individuals

@api_view(['GET', 'POST'])
def individuals(request):
    
    if request.method == 'GET':
        individual = Individual.objects.all()
    
        # member = Member.objects.get_queryset().filter(entity = user)
        
        serializer = IndividualSerializer(individual, many =True)
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        
        serializer = IndividualSerializer(data = request.data)
        
        if serializer.is_valid():
        
            serializer.validated_data['password'] = make_password(serializer.validated_data['password']) #hash the given password
            individual = Individual.objects.create(**serializer.validated_data)
            individual.save()

            serializer = IndividualSerializer(individual)
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

#Get the detail of a single individual by their ID

@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def individual_detail(request, pk):
    try:
        individual = Individual.objects.get(pk = pk)
    
    except Individual.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IndividualSerializer(individual)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    #Update the profile of the individual
    elif request.method == 'PUT':
        serializer = IndividualSerializer(individual, data = request.data, partial=True) #allows you to be able to update one field of the model

        if serializer.is_valid():
            
            #check if it's password change and hash the new password
            if "password" in serializer.validated_data.keys():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        
            serializer.save()

            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated profile",
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

    #delete the account
    elif request.method == 'DELETE':
        individual.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view([ 'POST'])
def individual_login(request):
    
    if request.method == "POST":
        
        user = authenticate(request, email = request.data['email'], password = request.data['password'])
        if user is not None:
        
            individual = Individual.objects.get(email = user.email)
            serializer = IndividualSerializer(individual)

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
