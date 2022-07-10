from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('telainicial/', views.telainicial, name='telainicial')

]