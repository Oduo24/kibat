from django.urls import path
from . import views

urlpatterns = [
    path('index/charges/', views.ChargeSheet, name='ChargeSheet'),



]



