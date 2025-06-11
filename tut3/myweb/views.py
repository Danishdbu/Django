from django.shortcuts import render

# Create your views here.

def learn_dj(req):
    return render(req, 'myweb/django.html')
    


