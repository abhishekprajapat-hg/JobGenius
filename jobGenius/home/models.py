from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    requirements = models.TextField(default='')
    
def __str__(self):
    return self.title