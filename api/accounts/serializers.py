# users/serializers.py
from rest_framework import serializers
from .models import CustomUser, Agent, Customer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Agent
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
