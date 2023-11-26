# accounts/urls.py
from rest_framework import routers
from .views import CustomUserViewSet, AgentViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'agents', AgentViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls



# # accounts/urls.py
# from rest_framework import routers
# from .views import CustomUserViewSet, AgentViewSet, CustomerViewSet, get_csrf_token
# from django.urls import path
#
# urlpatterns = [
#     path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
# ]
#
# router = routers.DefaultRouter()
# router.register(r'users', CustomUserViewSet)
# router.register(r'agents', AgentViewSet)
# router.register(r'customers', CustomerViewSet)
#
# urlpatterns += router.urls
