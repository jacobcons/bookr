from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def book_search(request):
    search = request.GET.get('search')
    return render(request, 'search.html', {"search": search})