from django.shortcuts import render
from student.forms import DemoForm

def demo_form(req):
    fm = DemoForm()
    return render(req, 'student/demo_form.html',{'form':fm})