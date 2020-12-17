from django.urls import path
from onlyapp import views

urlpatterns = [
    path('', views.onlyapp, name='onlyapp'),
]
