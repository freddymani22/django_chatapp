from django.contrib.auth.models import UserManager
from django.conf import settings
from django.db.models.query import QuerySet



# Create your models here.
class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset()
    
    def search(self, query):
        return self.get_queryset().filter(username__icontains = query)
    
    