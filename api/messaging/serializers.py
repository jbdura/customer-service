from rest_framework import serializers
from .models import Message, Response
from accounts.serializers import CustomerSerializer


class MessageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'
