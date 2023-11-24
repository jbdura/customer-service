from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255,  blank=True, null=True)

    # Add additional agent-specific fields
    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    # Add additional customer-specific fields
