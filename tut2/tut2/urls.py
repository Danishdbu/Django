
from django.contrib import admin
from django.urls import path
from myapp.views import learn
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj/', learn),
#    multiple url ke liye aaik page render kara sakte hai
    path('py/', learn,{'status':'ok'}), 
]
