from django.db import models


# Create your models here.
class user(models.Model):  # 继承

    name = models.CharField(max_length=30, unique="true")

    password = models.CharField(max_length=30)

    #class Meta:
    #d   db_table = 'user'
