from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reco
from .forms import NotesForm

# Create your views here.
class RecoCreate(CreateView):
    model = Reco
    fields = '__all__'
    success_url = '/recommendations'

class RecoUpdate(UpdateView):
    model = Reco
    fields = '__all__'

class RecoDelete(DeleteView):
    model = Reco
    success_url = '/recommendations'

def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def new_reco(req):
    return render(req, 'movies/new.html')

def my_recos(req):
    recos = Reco.objects.all()
    return render(req, 'movies/index.html', {'recos': recos})

def reco_detail(req, reco_id):
    reco = Reco.objects.get(id=reco_id)
    notes_form = NotesForm()
    return render(req, 'movies/detail.html', { 'reco': reco, 'notes_form': notes_form})

def add_note(request, reco_id):
    form = NotesForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.reco_id = reco_id
        new_note.save()
    return redirect('detail', reco_id=reco_id)