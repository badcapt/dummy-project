"""mydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from mydjangoapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^access_info/', include('mydjangoapp.urls')),
    url(r'^help/', views.help,name='help'),
    url(r'^user/', views.users, name='user'),
    url(r'^form/', views.form_view, name = 'form_name'),
    path('admin/', admin.site.urls),
]
