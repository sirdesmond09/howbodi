from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse

# Create your views here.

def add_question(request):
    file = 'n.txt'

    with open(file) as file_object: 
        lines = file_object.readlines() 
        
        for line in lines: 
            j = line.strip('\n').rsplit('\t')
            print(j[0], j[1])
            print(f'{j[-1]}\n')
            test_id = Test.objects.get(id=18)
            StressTestQuestion.objects.create(test = test_id, question = j[1], yes=j[-1], no = 0)
          
    return HttpResponse('This is a page') 