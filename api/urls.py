from django.urls import path
from .views import UsersearchApiView


urlpatterns = [
    path('users/',UsersearchApiView.as_view(), name='user-list' )
]