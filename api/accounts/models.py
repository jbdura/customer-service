from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields you need for both agents and customers
    pass


class Agent(models.Model):
    """
    This is agent user
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields specific to agents


class Customer(models.Model):
    """
    This is customer user
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields specific to customers
