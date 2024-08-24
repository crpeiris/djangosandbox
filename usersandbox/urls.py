from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name ='signup'),
    path('loggin_user', views.loggin_user, name ='loggin_user'),
    path('home', views.home, name ='home'),
]
