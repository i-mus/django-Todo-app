from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.index, name='index')
]
