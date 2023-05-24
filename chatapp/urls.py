from django.urls import path

from .views import index, chatroom

urlpatterns = [
    path('',index, name='home' ),
    path('<slug:slug>/',chatroom, name='chatroom'), 
    ]