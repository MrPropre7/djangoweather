
from django.contrib import admin
from django.urls import path
from . import views

#  from . --> from this current directory 
# he didnt put anything '' inside since the local host is / nothing
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    #path('about', views.about, name="about"),

]

# views.home --> views.py file in the function home
# name = home this is what django would look for
# --> when tell him to look for href ="{% url 'home' %}"