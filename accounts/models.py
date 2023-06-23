from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class CustomUser(AbstractUser):

       
    objects = CustomUserManager()


