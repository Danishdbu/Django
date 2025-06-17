from django.urls import path
from student.views import registration ,suc
urlpatterns = [
    path('register/',registration, name='registration'),
    path('success/',suc, name='success'),
  
]
