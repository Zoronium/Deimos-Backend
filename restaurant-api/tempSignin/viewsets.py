from rest_framework import viewsets
from .models import tempUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return tempUser.objects.all()
