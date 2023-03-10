from rest_framework import routers
from .viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r"user", UserViewSet, basename="user")
