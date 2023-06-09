from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async,async_to_sync
from accounts.models import CustomUser
from chatapp.models import ChatRoom,ChatMessage, PrivateMessage, PrivateContactList
from channels.exceptions import DenyConnection


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}".replace(" ", "_")

    

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.channel_name,
            self.room_group_name)

    async def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
      

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
            }
        )
        await self.save_message(username, room, message)


    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'requestUser':self.scope['user'].username==username
        }))


    @sync_to_async
    def save_message(self, username, room,message):
        user = CustomUser.objects.get(username=username)
        room = ChatRoom.objects.get(slug = room)
        ChatMessage.objects.create(user=user, room=room, message=message)






#private message

class PrivateMessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        current_user_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['other_id']
        if current_user_id> other_user_id:
             self.room_name = f'{current_user_id}_{other_user_id}'
        else:
            self.room_name = f'{other_user_id}_{current_user_id}'

       
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username_id = data['userName_id']
        request_user_id = data['requestUser_id']
      
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username_id': username_id,
                'request_user_id': request_user_id,
            }
        )

        await self.save_private_message(username_id, request_user_id, message )
    
    async def chat_message(self, event):
        message = event['message']
        username_id = event['username_id']
        request_user_id = event['request_user_id']
        await self.send(text_data=json.dumps({
            'message': message,
            'username_id': username_id,
            'request_user_id': request_user_id,
            'is_request_user': self.scope['user'].id == request_user_id,
        }))

    @sync_to_async
    def save_private_message(self, username_id, request_user_id, message):
        sender = CustomUser.objects.get(id=username_id)
        receiver = CustomUser.objects.get(id=request_user_id)
        PrivateMessage.objects.create(sender=sender, receiver=receiver, message=message)
        try:
            PrivateContactList.objects.get(created_by=sender, user_name=receiver)
        except PrivateContactList.DoesNotExist:
            PrivateContactList.objects.create(created_by=sender, user_name=receiver)


       



