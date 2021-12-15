from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv', views.pdf_view, name='cv'),
    path('projects', views.projects, name='projects'),
    path('music', views.music, name='music'),
    path('projects/bitcoin', views.bitcoin, name='bitcoin'),
    path('projects/squad', views.squad, name='squad'),
    path('projects/hubmap', views.hubmap, name='hubmap'),
    path('projects/music_generation', views.music_generation, name='music_generation'),
    path('projects/open_domain', views.open_domain, name='open_domain')
]