from rest_framework import routers
from menu.viewsets import MenuViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"cat", CategoryViewSet, basename="cat")
