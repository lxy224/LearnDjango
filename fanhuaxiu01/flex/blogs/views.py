# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
import datetime
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def home(request):
    now = datetime.datetime.now()
    return render_to_response('home.html', {'time': now}, context_instance=RequestContext(request))
    # return render_to_response('home.html', locals(), context_instance=RequestContext(request))
    # locals()表示把所有参数放进来
# request 是一个入的数据流，并未处理。context_instance=RequestContext(request)这种写法django对它进行了处理
#context_instance=RequestContext(request) django会自动把很多页面需要的参数添加到页面
#HttpResponse 无包装
#render 简单包装
#render_to_response 个性化和更加丰富的包装