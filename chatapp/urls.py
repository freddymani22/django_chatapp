from django.urls import path

from .views import index,chatroom,private_message_listview,private_message_detailview

urlpatterns = [
    path('',index, name='home' ),
    path('<slug:slug>/',chatroom, name='chatroom'), 
    path('private-message/<int:id>/', private_message_listview,name='private-message-list'),
    path('private-message/<int:id>/<int:other_id>/', private_message_detailview,name='private-message-detail'),

    ]