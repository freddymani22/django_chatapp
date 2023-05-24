from django.db import models
from django.urls import reverse

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)



    def get_absolute_url(self):
        return reverse('chatroom', kwargs={'slug':self.slug})