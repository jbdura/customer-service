from rest_framework import viewsets, permissions
from .models import CustomUser, Agent, Customer
from .serializers import CustomUserSerializer, AgentSerializer, CustomerSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user, including unauthenticated users
    authentication_classes = []  # No authentication for this viewset


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user, including unauthenticated users
    authentication_classes = []  # No authentication for this viewset


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user, including unauthenticated users
    authentication_classes = []  # No authentication for this viewset

########################################################################################################################


# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import CustomUser, Agent, Customer
# from .serializers import CustomUserSerializer, AgentSerializer, CustomerSerializer
#
#
# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#
#
# class AgentViewSet(viewsets.ModelViewSet):
#     queryset = Agent.objects.all()
#     serializer_class = AgentSerializer
#
#
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


#
#
# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import CustomUser, Agent, Customer
# from .serializers import CustomUserSerializer, AgentSerializer, CustomerSerializer
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.http import JsonResponse
#
#
# @ensure_csrf_cookie
# def get_csrf_token(request):
#     return JsonResponse({'csrfToken': 'success'})
#
#
# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#
#
# class AgentViewSet(viewsets.ModelViewSet):
#     queryset = Agent.objects.all()
#     serializer_class = AgentSerializer
#
#
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#
