from django.shortcuts import render
from django.http import HttpResponse

# 'Hello world' test app
def hello_world(request):
    return HttpResponse("Hello, world")