from django.urls import path

from .views import index,chatroom,private_message_listview,private_message_detailview, private_message_default_view

urlpatterns = [
    path('', private_message_default_view, name='home'),
    path('private-message/<int:id>/', private_message_listview,name='private-message-list'),
    path('private-message/<int:id>/<int:other_id>/', private_message_detailview,name='private-message-detail'),
    path('group-message/',index, name='group-chat' ),
    path('group-message/<slug:slug>/',chatroom, name='chatroom'), 
]