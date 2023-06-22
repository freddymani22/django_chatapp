from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.models import CustomUser


from .models import ChatRoom,ChatMessage,PrivateContactList,PrivateMessage

# Create your views here.
@login_required
def index(request):
    if request.method=='POST':
        room_name = request.POST.get('room-name')
        room_name =room_name.title()
        chat_room = ChatRoom.objects.get_or_create(name=room_name)
        context = {'chatrooms': chat_room}
        return render(request,'chatapp/index.html', context=context)

    chatrooms = ChatRoom.objects.all()
    context = {'chatrooms': chatrooms}
    return render(request,'chatapp/index.html', context=context)

@login_required
def chatroom(request,slug):

    chatroom = get_object_or_404(ChatRoom,slug=slug)
    messages = ChatMessage.objects.filter(room =chatroom).order_by('date')[0:30]
    return render(request, 'chatapp/detail.html', {"chatroom": chatroom,'messages':messages })

@login_required
def private_message_listview(request, id):
        if request.user.id == id:
            users = PrivateContactList.objects.filter(created_by = request.user.id)
            context = {'usernames': users}
            return render(request, 'chatapp/private-listview.html', context=context)
        else:
            return HttpResponse("<h1>YOU'RE NOT AUTHORIZED TO VIEW THIS PAGE</h1>")
       

@login_required
def private_message_detailview(request, other_id, id):
        if request.user.id == id:
            user_name_id = other_id
            other_user = CustomUser.objects.get(id = user_name_id)
            messages_sender = PrivateMessage.objects.filter(sender = id).filter(receiver = other_id)
            messages_receiver= PrivateMessage.objects.filter(sender = other_id).filter(receiver = id)
            messages = messages_sender | messages_receiver
            context= {'other_user':other_user, 'messages':messages.order_by('timestamp')}
            return render(request, 'chatapp/private-detailview.html', context=context)
        else:
            return HttpResponse("<h1>YOU'RE NOT AUTHORIZED TO VIEW THIS PAGE</h1>")
        
@login_required
def private_message_default_view(request):
     return redirect('private-message-list',id= request.user.id)