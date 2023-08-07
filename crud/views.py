from django.shortcuts import  render, redirect
from django.http import HttpResponse


def homepage(request):
    return render(request, "crud/index.html")
    return HttpResponse("Welcome to my website!")


    
