from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse



def learn_django(request):
    return HttpResponse("Hello Django")


# Create your views here.
