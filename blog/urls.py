from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('<str:slug>', views.post, name='post')
]