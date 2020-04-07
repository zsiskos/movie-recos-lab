from django.shortcuts import render
from django.http import HttpResponse

class Reco:
    def __init__(self, title, how_heard, where, description):
        self.title = title
        self.how_heard = how_heard
        self.where = where
        self.description = description

recos = [
    Reco('Fight Club', 'Zoe', 'NetFlix', 'A mind fuck movie'),
    Reco('Army of Darkness', 'James', 'NetFlix', 'The best B rated horror flick ever'),
    Reco('Onward', 'John', 'Disney', 'a funny feel good Disney flick'),
    Reco('The Outsider', 'James\'s work friend', 'Crave', 'same director as ozarks, basedo n stephen king, makes y ou think and creepy'),
    Reco('The Servant', 'James', 'AppleTV', 'so creepy, dir. by M. Night Shamalaman'),
    Reco('Bombshell', 'Ads', 'GooglePlay', 'true story, strong female characters'),
    Reco('House of 1000 Corpses', 'Joe', 'Netflix', 'scary AF'),
]




# Create your views here.
def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def new_reco(req):
    return render(req, 'movies/new.html')

def my_recos(req):
    return render(req, 'movies/index.html', {'recos': recos})
