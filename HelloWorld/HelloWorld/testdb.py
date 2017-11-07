# -*- coding: UTF-8 -*-。
from django.http import HttpResponse
from TestModel.models import Test

def testdb(requesr):
    test1 = Test(name="runoob")
    test1.save()
    return HttpResponse("<p>add success</p>")