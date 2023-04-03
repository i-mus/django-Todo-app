from django.db import models

# Create your models here.

class Task(models.Model):
    username = models.CharField(max_length=200,default="js")
    name = models.CharField(max_length=200)
    priority = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
