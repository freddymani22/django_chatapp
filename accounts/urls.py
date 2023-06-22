from django.urls import path

from .views import register,login_view,logout_view, profile_detail,profile


urlpatterns = [
    path('register/',register, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('profile/',profile, name='profile'),
    path('profile/<int:id>/',profile_detail, name='profile-detail')
]