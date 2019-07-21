from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'index.html', locals())


def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request, 'images.html', locals())



def images(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request, 'images.html', locals())


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'category.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html', {"message": message})


def getcat(request, catid):
    category = get_object_or_404(Category, pk=catid)
    title = category.Name
    name = category.Name
    images = category.images.all()
    return render(request, 'images.html', locals())
