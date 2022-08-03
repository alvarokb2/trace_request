from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=40, default="Nuevo")
    
    def __str__(self):
        return self.name