from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This would be the About page.")

def about_me(request):
    """Compatibility view used by project URLs.

    Returns a simple About page response. Keep both `index` and `about_me`
    so either can be referenced by different URL configs.
    """
    return HttpResponse("About: This is a simple about page.")