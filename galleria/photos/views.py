from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Images, Category, Location
# Create your views here.
def index(request):
    images = Images.all_images()
    return render(request, 'main.html', {"images":images})
