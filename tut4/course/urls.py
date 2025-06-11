from django.urls import path
from course.views import learn_dj

urlpatterns = [
 path('dj/', learn_dj)
]
