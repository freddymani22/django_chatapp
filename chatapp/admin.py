from django.contrib import admin
from .models import ChatRoom,ChatMessage,PrivateContactList,PrivateMessage


# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(ChatMessage)
admin.site.register(PrivateContactList)
admin.site.register(PrivateMessage)