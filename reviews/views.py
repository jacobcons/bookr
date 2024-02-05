from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


# Create your views here.
def index(request):
    return render(request, "base.html")


def book_search(request):
    search = request.GET.get("search")
    return render(request, "search.html", {"search": search})


def welcome(request):
    html_str = f"<html><h1>Welcome to bookr</h1><p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(html_str)
