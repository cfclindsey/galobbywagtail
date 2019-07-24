from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createnotice', views.create_notice, name='create_notice')
]
