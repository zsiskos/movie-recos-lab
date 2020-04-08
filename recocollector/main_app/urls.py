from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recommendations/', views.my_recos, name='my_recos'),
    path('new/', views.RecoCreate.as_view(), name='new_reco'),
    path('recommendations/<int:reco_id>/', views.reco_detail, name='detail')
]