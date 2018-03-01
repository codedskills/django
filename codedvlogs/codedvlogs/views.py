from django.shortcuts import render

#   create functions

def about(request):
    return render(request,'about.html')

def homepage(request):
    return render(request,'home.html')
