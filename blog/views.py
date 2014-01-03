from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Coming soon! You stay classy San Diego.")
