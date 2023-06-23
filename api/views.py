from rest_framework import generics
from accounts.models import CustomUser
from .serializers import UserSerializer
from rest_framework import permissions
# Create your views here.
class UsersearchApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        print(q)
        results = CustomUser.objects.none()
        if q is not None:
            return CustomUser.objects.search(query=q)
        return results