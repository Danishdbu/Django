from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myapp_math(request):
    a = 10
    b= 10
    c= a+b
    return HttpResponse(c)