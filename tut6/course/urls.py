from django.urls import path
from course.views import learn_dj 
from course.views import learn_py

urlpatterns = [
    path('dj/',learn_dj,name='django'),
    path('py/',learn_py,name='python'),
]