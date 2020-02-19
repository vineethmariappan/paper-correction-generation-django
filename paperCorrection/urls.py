from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('validate', views.validate, name='validate'),
    path('index', views.index, name='index'),
]