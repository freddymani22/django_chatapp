from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from .forms import CustomRegister
from .models import CustomUser



# Create your views here.
def register(request):
    form = CustomRegister(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
            logout(request)
            return redirect('login')



def profile(request):
     if request.method == 'POST':
          profile_pic = request.FILES.get('profile_pic')
          user = CustomUser.objects.get(username= request.user)
          user.profile_pic = profile_pic
          user.save()
          return redirect('profile')
     return render(request, 'accounts/profile.html')


def profile_detail(request, id):
     user = CustomUser.objects.get(id = id)

     return render(request, 'accounts/profile-detail.html',{'user':user})
     