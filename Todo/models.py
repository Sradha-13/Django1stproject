from django.db import models
from django.db.models.base import Model

# Create your models here.
class Todo(models.Model):
    name=models.CharField(max_length=40)
    due_date=models.DateField()
    
    def __str__(self):
        return self.name