from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from main.models import *
from .serializers import *


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def addiction_questions_list(request):
    if request.method == 'GET':
        questions = AddictionQuestion.objects.all()
        serializer = AddictionSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AddictionSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def addiction_question_detail(request, pk):
    try:
        question = AddictionQuestion.objects.get(pk = pk)
    
    except AddictionQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddictionSerializer(question)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AddictionSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def anxiety_questions_list(request):
    if request.method == 'GET':
        questions = AnxietyQuestion.objects.all()
        serializer = AnxietySerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AnxietySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def anxiety_question_detail(request, pk):
    try:
        question = AnxietyQuestion.objects.get(pk = pk)
    
    except AnxietyQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AnxietySerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AnxietySerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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


    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def dass_questions_list(request):
    if request.method == 'GET':
        questions  = D_A_S_SQuestion.objects.all()
        serializer = D_A_S_SSerializer(questions, many=True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = D_A_S_SSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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


@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def dass_question_detail(request, pk):

    try:
        question = D_A_S_SQuestion.objects.get(pk=pk)

    except D_A_S_SQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = D_A_S_SSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = D_A_S_SSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def depression_questions_list(request):
    if request.method == 'GET':
        questions = DepressionQuestion.objects.all()
        serializer = DepressionSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DepressionSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def depression_question_detail(request, pk):
    try:
        question = DepressionQuestion.objects.get(pk = pk)
    
    except DepressionQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepressionSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DepressionSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def hostility_questions_list(request):
    if request.method == 'GET':
        questions = HostilityQuestion.objects.all()
        serializer = HostilitySerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = HostilitySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def hostility_question_detail(request, pk):
    try:
        question = HostilityQuestion.objects.get(pk = pk)
    
    except HostilityQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HostilitySerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = HostilitySerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def insomnia_questions_list(request):
    if request.method == 'GET':
        questions = InsomniaQuestion.objects.all()
        serializer = InsomniaSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = InsomniaSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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


@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def insomnia_question_detail(request, pk):
    try:
        question = InsomniaQuestion.objects.get(pk = pk)
    
    except InsomniaQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InsomniaSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = InsomniaSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def interpersonal_sensitivity_questions_list(request):
    if request.method == 'GET':
        questions = InterpersonalSensitivityQuestion.objects.all()
        serializer = InterpersonalSensitivitySerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = InterpersonalSensitivitySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def interpersonal_sensitivity_question_detail(request, pk):
    try:
        question = InterpersonalSensitivityQuestion.objects.get(pk = pk)
    
    except InterpersonalSensitivityQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InterpersonalSensitivitySerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = InterpersonalSensitivitySerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def neuroticism_questions_list(request):
    if request.method == 'GET':
        questions = NeuroticismQuestion.objects.all()
        serializer = NeuroticismSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = NeuroticismSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def neuroticism_question_detail(request, pk):
    try:
        question = NeuroticismQuestion.objects.get(pk = pk)
    
    except NeuroticismQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NeuroticismSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NeuroticismSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def ocd_questions_list(request):
    if request.method == 'GET':
        questions = O_C_DQuestion.objects.all()
        serializer = O_C_DSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = O_C_DSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def ocd_question_detail(request, pk):
    try:
        question = O_C_DQuestion.objects.get(pk = pk)
    
    except O_C_DQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = O_C_DSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = O_C_DSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def paranoia_questions_list(request):
    if request.method == 'GET':
        questions = ParanoiaQuestion.objects.all()
        serializer = ParanoiaSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ParanoiaSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def paranoia_question_detail(request, pk):
    try:
        question = ParanoiaQuestion.objects.get(pk = pk)
    
    except ParanoiaQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParanoiaSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ParanoiaSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def parent_pediatric_symptom_questions_list(request):
    if request.method == 'GET':
        questions = ParentsPediatricSymptomQuestion.objects.all()
        serializer = ParentsPediatricSymptomSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ParentsPediatricSymptomSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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




@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def parent_pediatric_symptom_question_detail(request, pk):
    try:
        question = ParentsPediatricSymptomQuestion.objects.get(pk = pk)
    
    except ParentsPediatricSymptomQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParentsPediatricSymptomSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ParentsPediatricSymptomSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def personal_health_questions_list(request):
    if request.method == 'GET':
        questions = PersonalHealthQuestion.objects.all()
        serializer = PersonalHealthSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        serializer = PersonalHealthSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def personal_health_question_detail(request, pk):
    try:
        question = PersonalHealthQuestion.objects.get(pk = pk)
    
    except PersonalHealthQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalHealthSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PersonalHealthSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def personality_questions_list(request):
    if request.method == 'GET':
        questions = PersonalityQuestion.objects.all()
        serializer = PersonalitySerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PersonalitySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def personality_question_detail(request, pk):
    try:
        question = PersonalityQuestion.objects.get(pk = pk)
    
    except PersonalityQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalitySerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PersonalitySerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def phobia_questions_list(request):
    if request.method == 'GET':
        questions = PhobiaQuestion.objects.all()
        serializer = PhobiaSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        serializer = PhobiaSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def phobia_question_detail(request, pk):
    try:
        question = PhobiaQuestion.objects.get(pk = pk)
    
    except PhobiaQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhobiaSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PhobiaSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def psychoticism_questions_list(request):
    if request.method == 'GET':
        questions = PsychoticismQuestion.objects.all()
        serializer = PsychoticismSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PsychoticismSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def psychoticism_question_detail(request, pk):
    try:
        question = PsychoticismQuestion.objects.get(pk = pk)
    
    except PsychoticismQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PsychoticismSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PsychoticismSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def sleep_apnea_questions_list(request):
    if request.method == 'GET':
        questions = SleepApneaQuestion.objects.all()
        serializer = SleepApneaSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SleepApneaSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def sleep_apnea_question_detail(request, pk):
    try:
        question = SleepApneaQuestion.objects.get(pk = pk)
    
    except SleepApneaQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SleepApneaSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SleepApneaSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def somatization_questions_list(request):
    if request.method == 'GET':
        questions = SomatizationQuestion.objects.all()
        serializer = SomatizationSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SomatizationSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def somatization_question_detail(request, pk):
    try:
        question = SomatizationQuestion.objects.get(pk = pk)
    
    except SomatizationQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SomatizationSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SomatizationSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def stress_test_questions_list(request):
    if request.method == 'GET':
        questions = StressTestQuestion.objects.all()
        serializer = StressTestSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StressTestSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def stress_test_question_detail(request, pk):
    try:
        question = StressTestQuestion.objects.get(pk = pk)
    
    except StressTestQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StressTestSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StressTestSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def youth_pediatric_symptom_questions_list(request):
    if request.method == 'GET':
        questions = YouthsPediatricSymptomQuestion.objects.all()
        serializer = YouthsPediatricSymptomSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = YouthsPediatricSymptomSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated]) 
def youth_pediatric_symptom_question_detail(request, pk):
    try:
        question = YouthsPediatricSymptomQuestion.objects.get(pk = pk)
    
    except YouthsPediatricSymptomQuestion.DoesNotExist:
        data = {
                'status'  : status.HTTP_404_NOT_FOUND,
                'message' : "Unsuccessful",
                'data' : "Table does not exist",
            }

        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YouthsPediatricSymptomSerializer(question)
        
        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = YouthsPediatricSymptomSerializer(question, data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully updated question",
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

    elif request.method == 'DELETE':
        question.delete()

        data = {
                'status'  : status.HTTP_204_NO_CONTENT,
                'message' : "Deleted Successfully"
            }

        return Response(data, status = status.HTTP_204_NO_CONTENT)



#get all tests
@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication,])
# @permission_classes([IsAuthenticated])
def test_list(request):
    if request.method == 'GET':
        questions = Test.objects.all()
        serializer = TestSerializer(questions, many =True)

        data = {
                'status'  : status.HTTP_200_OK,
                'message' : "Successful",
                'data' : serializer.data,
            }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TestSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'status'  : status.HTTP_201_CREATED,
                'message' : "Successfully added question",
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


