from django.urls import path
from course.views import learn_dj 
from course.views import learn_py

urlpatterns = [
    path('dj/',learn_dj),
    path('py/',learn_py),
]