from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Reco

# Create your views here.
def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def new_reco(req):
    return render(req, 'movies/new.html')

def my_recos(req):
    recos = Reco.objects.all()
    return render(req, 'movies/index.html', {'recos': recos})

class RecoCreate(CreateView):
    model = Reco
    fields = '__all__'
