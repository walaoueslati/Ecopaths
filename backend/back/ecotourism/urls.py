from django.contrib import admin
from django.urls import path,include
from .views import authView
from .views import home

urlpatterns = [
    path('', home , name='home'),
    path('signup/', authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),

]
