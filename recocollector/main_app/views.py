from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('<h1>this works</h1>')

def about(req):
    return HttpResponse('<h1>About page</>')

def new_reco(req):
    return HttpResponse('<h1>Add a New Recommendation</h1>')

def my_recos(req):
    return HttpResponse('<h1>My Recommendations</h1>')
