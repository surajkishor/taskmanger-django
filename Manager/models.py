from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tasks(models.Model):
    task = models.CharField(max_length=100)
    userr = models.ForeignKey(User, on_delete=models.CASCADE)
