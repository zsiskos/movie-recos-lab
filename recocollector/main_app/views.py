from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def new_reco(req):
    return render(req, 'movies/new.html')

def my_recos(req):
    return render(req, 'movies/index.html')
