from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name+' '+self.surname
