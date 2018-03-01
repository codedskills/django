from django.http import HttpResponse
from django.shortcuts import render

#   create a function

def about(request):
    return HttpResponse("Hello This is CodedVlog First Test")

def homepage(request):
    return HttpResponse("Hello Welcome To CodedVlogs")
