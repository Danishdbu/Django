from django.shortcuts import render
from student.forms import Registration,Login
# Create your views here.
def registration(req):
    fm = Registration()
    return render(req, 'student/registration.html',{'form':fm})

def login(req):
    # lg= Login(auto_id='md_%s')
    # lg= Login(auto_id=True)
    lg= Login(label_suffix=' ')
    return render(req, 'student/login.html',{'form':lg})
