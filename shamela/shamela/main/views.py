from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import resolve
from .forms import BookForm

# Create your views here.
def index(request):
    books = Books.objects.all()
    categories = Categories.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def category_page(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main/categories.html', context)


def books_list(request, id):
    set1 = Categories.objects.get(id=id)
    books = set1.books_set.all()
    context = {
        'books': books
    }
    return render(request, 'main/BooksByCategories.html', context)


def books_description(request, id):
    book = Books.objects.get(id=id)
    b = book
    b.views +=1
    b.save()

    current_url = resolve(request.path_info).url_name
    context = {
        'book': book,
        'current_url': 'http://127.0.0.1:8000/'+current_url+'/'+str(book.id)
    }
    return render(request, 'main/BooksDescription.html', context)


def get_newBooks(request):
    books = Books.objects.order_by('-created_at')
    context = {
        'books' : books
    }
    return render(request, 'main/newBooks.html', context)


def popular_books(request):
    books = Books.objects.order_by('-views')
    Books.objects.exclude(phone_book_file=True)
    context = {
        'books': books
    }

    return render(request, 'main/popularBooks.html', context)


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'main/upload_book.html',{'form': form})


def aurthor_details(request, pk):
    aurthor = AurthorsPro.objects.get(id=pk)
    books = Books.objects.filter(aurthor=aurthor)
    context ={
        'aurthor': aurthor,
        'books': books
    }

    return render(request, 'main/aurthor_page.html', context)


def phone_books(request):
    books = Books.objects.exclude(phone_book_file='')

    return render(request, 'main/phone_copies.html', {'books': books})


def BooksByUsers(request):
    books = UserBooks.objects.filter(status=1)

    return render(request, 'main/users_books.html', {'books': books})


def SearchBooks(request):
    term = request.GET.get('q')
    results = Books.objects.filter(name__icontains=term) | Books.objects.filter(aurthor__name__icontains=term)

    return render(request, 'main/search_results.html', {'result': results})