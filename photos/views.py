from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Images, Category, Location
# Create your views here.
def index(request):
    images = Images.all_images()
    return render(request, 'main.html', {"images":images})

def search(request):
    print(request.GET)
    print(request.GET)
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
    return render(request,'search.html')
