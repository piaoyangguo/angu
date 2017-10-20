from django.shortcuts import render_to_response
from models import Book
# Create your views here.

def index(request):
    res = {}
    res['books'] = Book.objects.all()
    return render_to_response('index.html', res)