# -*- coding: UTF-8 -*-。

from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
# 类名代表了数据库表名，且继承了models.Model类里面的字段代表数据表中的字段name，数据类型则由CharFiled（相当于varchar），DateField（相当于datetime）， max_length 参数限定长度。python manage.py makemigrations TestModel

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name