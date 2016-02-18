from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("(" + request.META["CONTENT_TYPE"] + ") Hello, world. You're at the polls index.")
