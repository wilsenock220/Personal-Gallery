from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from .models import Image, Location
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    return render(request, 'index.html', locals())


def gallery(request):
    images = Image.objects.all()
    location = Location.objects.all()
    print(location)
    return render(request, 'images.html', {"images": images, "location": location})

def get_category(request):
  category_results = Category.objects.all()
  location_results = Location.objects.all()
  return render(request, 'index.html', {'category_results': category_results, 'location_results': location_results})


def get_location(request):
  category_results = Category.objects.all()
  location_results = Location.objects.all()
  return render(request, 'index.html', { 'category_results': category_results, 'location_results': location_results})

def search_results(request):

    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def search_by_location(request, location):
    locations = Location.objects.all()
    images = Image.search_by_location(location)
    print(images)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title': title, 'images': images, 'locations': locations})
