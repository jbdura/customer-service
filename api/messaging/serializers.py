from rest_framework import serializers
from .models import Message, Response
from accounts.serializers import CustomerSerializer, AgentSerializer


class MessageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()

    class Meta:
        model = Response
        fields = '__all__'
