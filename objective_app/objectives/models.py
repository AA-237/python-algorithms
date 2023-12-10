from django.db import models

# Create your models here.

class Objectives(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateField(null=False) # indicates it is a required field with a nul False
    end_date = models.DateField(null=True)
    
    
    def __str__(self):
        return f"{self.title} ({self.description})"