from django.shortcuts import render

# Create your views here.
def learn_dj(req):
    return render(req, 'course/django.html')

def learn_py(req):
    return render(req, 'course/python.html')