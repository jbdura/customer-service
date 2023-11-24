# accounts/urls.py
from rest_framework import routers
from .views import CustomUserViewSet, AgentViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'agents', AgentViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls
