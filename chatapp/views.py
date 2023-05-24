from django.shortcuts import render,get_object_or_404


from .models import ChatRoom

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()
    context = {'chatrooms': chatrooms}
    return render(request,'chatapp/index.html', context=context)



def chatroom(request,slug):
    chatroom = get_object_or_404(ChatRoom,slug=slug)
    return render(request, 'chatapp/detail.html', {"chatroom": chatroom})

