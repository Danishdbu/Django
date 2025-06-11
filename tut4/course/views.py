from django.shortcuts import render
from datetime import date, datetime
# Create your views here.

# 1- VARIABLE

# def learn_dj(req):
    
#     return render(req, 'course/django.html',context={'name':'Django'})

# 1- FILTER
# def learn_dj(req):
#     return render(req, 'course/django.html',context={'name':'Django'})

# Date and Time
# def learn_dj(req):
#     d = datetime.now()
#     return render(req, 'course/django.html',context={'dt':d})

# tag 
def learn_dj(req):
    d = datetime.now()
    return render(req, 'course/django.html',context={'nm':True,'range': range(6)})