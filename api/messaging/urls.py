from rest_framework import routers
from .views import MessageViewSet, ResponseViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = router.urls

# # messaging/urls.py
# from rest_framework import routers
# from .views import MessageViewSet, ResponseViewSet
#
# router = routers.DefaultRouter()
# router.register(r'messages', MessageViewSet)
# router.register(r'responses', ResponseViewSet)
#
# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
