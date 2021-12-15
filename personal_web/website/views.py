from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

# def cv(request):
#     return render(request, 'website/cv.html')

def projects(request):
    return render(request, 'website/projects.html')

def music(request):
    return render(request, 'website/music.html')

def pdf_view(request):
    try:
        return FileResponse(open('static/cv.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def bitcoin(request):
    return render(request, 'website/projects/bitcoin.html')

def hubmap(request):
    return render(request, 'website/projects/hubmap.html')

def music_generation(request):
    return render(request, 'website/projects/music_generation.html')

def squad(request):
    return render(request, 'website/projects/squad.html')

def open_domain(request):
    return render(request, 'website/projects/open_domain.html')