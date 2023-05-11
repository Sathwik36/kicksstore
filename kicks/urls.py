"""
URL configuration for kicks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

admin.site.site_header = "KICKS store"
admin.site.site_title = "Welcome to KICKS store"
admin.site.index_title = "Welcome to  store "

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('kicksapp.urls')),
    path('verify',include('kicksapp.urls')),
    path('home',include('kicksapp.urls')),
    path('delivery',include('kicksapp.urls')),
    path('deals',include('kicksapp.urls')),
    path('new',include('kicksapp.urls')),
    path('feedback',include('kicksapp.urls')),
    path('submit',include('kicksapp.urls')),
    path('buy',include('kicksapp.urls'))

]
