from django.urls import path
from myweb.views import learn_dj

urlpatterns = [
 path('dj/', learn_dj)
]
