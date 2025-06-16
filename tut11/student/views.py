from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.forms import Registration 
# Create your views here.
def registration(req):
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name)
            print(email)
            print(password)
            return HttpResponseRedirect('/student/success')
    else:
        form = Registration()
    return render(req, 'student/registration.html',{'form':form})

def suc(req):
    return render(req, 'student/success.html')



    
