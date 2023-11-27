# messaging/urls.py
from django.urls import path
from .views import CustomerMessagesView, AnswerMessageView, MessageViewSet, ResponseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('customers/<int:customer_pk>/messages/', CustomerMessagesView.as_view(), name='customer-messages'),
    path('customers/<int:customer_pk>/answer-message/', AnswerMessageView.as_view(), name='answer-message'),
]

urlpatterns += router.urls


########################################################################################################################


# from django.urls import path
# from .views import CustomerMessagesView, AnswerMessageView, MessageViewSet, ResponseViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'messages', MessageViewSet)
# router.register(r'responses', ResponseViewSet)
#
# urlpatterns = [
#     path('customers/<int:customer_pk>/messages/', CustomerMessagesView.as_view(), name='customer-messages'),
#     path('customers/<int:customer_pk>/answer-message/', AnswerMessageView.as_view(), name='answer-message'),
# ]
#
# urlpatterns += router.urls
#
#######################################################################################################################
#
# # from rest_framework import routers
# # from .views import MessageViewSet, ResponseViewSet
# #
# # router = routers.DefaultRouter()
# # router.register(r'messages', MessageViewSet)
# # router.register(r'responses', ResponseViewSet)
# #
# # urlpatterns = router.urls
#
#
#
#######################################################################################################################
# # from rest_framework import routers
# # from .views import MessageViewSet, ResponseViewSet
# #
# # router = routers.DefaultRouter()
# # router.register(r'messages', MessageViewSet)
# # router.register(r'responses', ResponseViewSet)
# #
# # urlpatterns = [
# #     path('api/', include(router.urls)),
# # ]
