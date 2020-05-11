from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {"title":"Home"})

def another_page(request):
    return render(request, 'another_site.html', {"title" : "Site"})

def particle_page(request):
    return render(request, 'particles.html', {"title": "particle"})

def main_page(request):
    return render(request, 'homepage.html', {"title":"Insider Page"})