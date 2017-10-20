#coding: utf8
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField("名字", max_length=200)
    avar = models.ImageField("头像", upload_to='uploads/%Y/%m/%d')