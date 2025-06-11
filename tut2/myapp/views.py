from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn(req,**kwargs):
    status = kwargs.get('status','not define')

    return HttpResponse(f'<h1>Hello Django {status}</h1> ')