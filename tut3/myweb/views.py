from django.shortcuts import render

# Create your views here.

def learn_dj(req):
    # here we write business logic
    coursename={'name':'Pyhton'}
    # return render(req, 'myweb/django.html',context= coursename)
    # return render(req, 'myweb/django.html',{'name':'Pyhton'})
    return render(req, 'myweb/django.html',coursename)
    


