from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models
from django.conf import settings
from PIL import Image
from django.db.models.signals import post_save
User = settings.AUTH_USER_MODEL

# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/', default='default.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path).convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    objects = CustomUserManager()


