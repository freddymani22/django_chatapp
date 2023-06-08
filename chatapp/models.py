from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.utils.text import slugify
from accounts.models import CustomUser



# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'slug':self.slug})
    
class PrivateContactList(models.Model):
    created_by = models.ForeignKey(CustomUser,related_name='created_by', on_delete=models.CASCADE)
    user_name = models.ForeignKey(CustomUser,related_name='user_name', on_delete=models.CASCADE)


    def __str__(self):
        return self.created_by.username

    def get_absolute_private_listview_url(self):
        return reverse('private-message-list', kwargs={'id':self.user_name})
    

class PrivateMessage(models.Model):
    sender = models.ForeignKey(CustomUser,related_name='sent_messages',on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,related_name='received_messages',on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)



def slug_chatroom(instance,created, *args, **kwargs):
    if created:
        instance.slug= slugify(instance.name)
        instance.save()

post_save.connect(slug_chatroom,sender=ChatRoom)