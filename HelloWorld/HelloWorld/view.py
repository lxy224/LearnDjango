from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello']="hello world!hahaha"
    # return HttpResponse("Hello World!");
    return render(request, "hello.html", context)