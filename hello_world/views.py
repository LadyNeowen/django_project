from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Simple index view that responds differently to POST vs other methods.

    - POST -> short confirmation message
    - GET/other -> Hello world message
    """
    if request.method == 'POST':
        return HttpResponse("You must have POSTed something.")
    else:
        return HttpResponse(request.method)