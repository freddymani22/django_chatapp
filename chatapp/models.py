from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.utils.text import slugify

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'slug':self.slug})
    

    


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)



def slug_chatroom(instance,created, *args, **kwargs):
    if created:
        slug = slugify(instance.name)
        instance.slug= f'{slug}-{instance.id}'
        instance.save()

post_save.connect(slug_chatroom,sender=ChatRoom)