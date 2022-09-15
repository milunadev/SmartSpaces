from django.shortcuts import render
from django.http import HttpResponse 


def index(request): 
    return render(request, 'index2.html', context={'text': 'Hello world'})

def index_oficial(request): 
    return render(request, 'index_oficial.html', context={'text': 'Hello world'})

def landing(request): 
    return render(request, 'environment.html', context={'text': 'Hello world'})