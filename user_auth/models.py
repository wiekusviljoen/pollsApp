from django.db import models

# Create your models here.
# yourapp/models.py
from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username
