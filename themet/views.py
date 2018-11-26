# from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
# from themet.forms import BookForm
from themet.models import Book
# from django.contrib.auth.decorators import login_required
# from django.http import Http404


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books, })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })


def browse_by_title(request, initial=None):
    if initial:
        books = Book.objects.filter(title__istartswith=initial).order_by('title')
    else:
        books = Book.objects.all().order_by('title')
    return render(request, 'search/search.html', {
        'books': books,
        'initial': initial,
    })
