from django.shortcuts import render

# Create your views here.

# 1- VARIABLE

def learn_dj(req):
    
    return render(req, 'course/django.html',context={'name':'Django'})
