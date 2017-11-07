# -*- coding: UTF-8 -*-。
from django.http import HttpResponse
from django.shortcuts import render_to_response

#form
def search_form(request):
    return render_to_response('search_form.html')

#receive data
def search(request):
    request.encoding="utf-8"
    if 'q' in request.GET:
        message = "what you searched is: " + request.GET['q']
    else:
        message = 'you submmited empty form'
    return  HttpResponse(message)