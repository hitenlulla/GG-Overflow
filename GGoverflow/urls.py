"""GGoverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from data import views
from data.views import collectionv

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('temp/',views.temp,name='temp'),
    path('about/',views.about,name='about'),
    path('collection/',collectionv.as_view(),name='collection'),
    path('signup/',include('django.contrib.auth.urls')),
    path('signup/',include('users.urls')),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.cart2,name='cart'),
    path('update_item/',views.updateitem, name ='update_item'),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

