from django.shortcuts import render
from student.models import Profile
# Create your views here.
def home(req):
    students = Profile.objects.all()
    return render(req, 'student/all.html',{'students': students})