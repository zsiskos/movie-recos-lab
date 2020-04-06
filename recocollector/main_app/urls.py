from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new/', views.new_reco, name='new_reco'),
    path('recommendations/', views.my_recos, name='my_recos'),
]