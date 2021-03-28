from django.shortcuts import render
from djago.https import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world, you are index my app")