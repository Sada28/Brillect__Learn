"""Learn URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashpage),
    path('index',views.Indexpage,name='ind'),
    # path('',views.Indexpage),
    path('Registration',views.userreg,name='reg'),
    path('Login',views.loginpage,name='Log'),
    path('python',views.pypage,name='py'),
    path('ml',views.ml,name='ml'),
    path('java',views.java,name='java'),
    path('web',views.web,name='web'),
    path('android',views.android,name='android'),
    path('clang',views.clang,name='clang'),
    path('cpp',views.cpp,name='cpp'),
]