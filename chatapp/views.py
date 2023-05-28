from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import ChatRoom,ChatMessage

# Create your views here.
@login_required
def index(request):
    chatrooms = ChatRoom.objects.all()
    context = {'chatrooms': chatrooms}
    return render(request,'chatapp/index.html', context=context)

@login_required
def chatroom(request,slug):
    chatroom = get_object_or_404(ChatRoom,slug=slug)
    messages = ChatMessage.objects.filter(room =chatroom).order_by('date')[0:30]
    return render(request, 'chatapp/detail.html', {"chatroom": chatroom,'messages':messages })

