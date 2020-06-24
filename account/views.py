from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def add_user(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many =True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
           

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



