from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from data import views
from data.views import collectionv
from django.urls import path
from .views import UserRegisterView
urlpatterns = [

            #path('register/',UserRegisterView.as_view(), name='register'),
            path('',UserRegisterView.as_view(), name='register'),
]

