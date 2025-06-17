from student.models import Profile
from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.forms import Registration 
# Create your views here.
def registration(req):
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw= form.cleaned_data['password']
            # save data into databases
            user = Profile(name=nm,email=em,password=pw)
            user.save()
            return HttpResponseRedirect('/student/success')
    else:
        form = Registration()
    return render(req, 'student/registration.html',{'form':form})

def suc(req):
    return render(req, 'student/success.html')



    
