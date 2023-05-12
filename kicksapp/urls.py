from django.contrib import admin
from django.urls import path
from kicksapp import views

urlpatterns = [
    path('',views.login,name="login"),
    path('verify',views.verify,name="verify"),
    path('home',views.home,name="home"),
    path('deals',views.deals,name="deals"),
    path('new',views.new,name="new"),
    path('feedback',views.feedback,name="feedback"),
    path('submit',views.submit,name="submit"),
    path('buy',views.buy,name="buy"),
    path('mail',views.mail,name="mail")
]