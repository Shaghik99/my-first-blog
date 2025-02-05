from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.nature, name='nature'),
    path('', views.street, name='street'),
    ]