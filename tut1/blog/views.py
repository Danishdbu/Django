from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myWeb(request):
    return HttpResponse('hello world')
def myWeb_html(request):
    return HttpResponse('<h1>hello HTML</h1>')

def myWeb_math(request):
    a = 10
    b= 12
    c= a+b
    return HttpResponse(c)