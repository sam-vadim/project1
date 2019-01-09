from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(null=True, verbose_name="Возраст")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")

    def __str__(self):
        return self.name+' '+self.surname

    class Meta:
        verbose_name = "Человека"
        verbose_name_plural = "Люди"
