from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Response
from .serializers import MessageSerializer, ResponseSerializer


# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
