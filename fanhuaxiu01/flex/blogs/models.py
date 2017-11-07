# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField("tile of article",max_length=50)
    writer = models.CharField("author of article",max_length=50)
    created_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    content = models.TextField()
    is_show = models.BooleanField(default=False)

    class Meta:
        db_table = "Article" #db table name
    def __str__(self):
        #给每个实例取名字
        return self.title
