from django.contrib import admin
from .models import CustomUser, Customer, Agent

# Register your models here.
admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(CustomUser)
