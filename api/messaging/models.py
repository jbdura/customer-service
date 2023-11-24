from django.db import models
from accounts.models import Agent, Customer


# Create your models here.

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)


class Response(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
