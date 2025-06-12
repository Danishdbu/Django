from django.shortcuts import render


def learn_dj(req):
    
    return render(req, 'course/django.html',{'nm':'Django'})
