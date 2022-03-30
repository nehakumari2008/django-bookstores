from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

import requests

# Create your views here.
import books_store
from books_store.forms import StoreForm, RegisterForm, BookForm
from books_store.models import Store, Book

def index(request):
    return HttpResponseRedirect('/store/')

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/store/')
        else:
            form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    else:
        return HttpResponseRedirect('/store/')

@login_required
def get_store(request):
    stores = Store.objects.all().filter(user=request.user)
    books = Book.objects.all().filter(user=request.user)
    meta = {'bookstore_no': len(stores),
            'books_no': len(books)}

    return render(request, 'books_store/store.html', {'stores': stores, 'user': request.user, 'meta': meta})

@login_required
def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            store = Store(name=name, user=request.user)
            store.save()
            return HttpResponseRedirect('/store/')
    else:
        form = StoreForm()
    return render(request, 'books_store/store_create.html', {'form': form})

@login_required
def edit_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST,instance=store)
        name = form.data['name']
        store.name = name
        store.save()
        return HttpResponseRedirect('/store/')
    else:
        form = StoreForm(instance=store)
    return render(request, 'books_store/store_edit.html', {'form': form, 'store': store})


@login_required
def delete_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return HttpResponseRedirect('/store/')


@login_required()
def create_book(request, store_id):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            store = get_object_or_404(Store, pk=store_id)
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            price = form.cleaned_data['price']
            no_of_copies = form.cleaned_data['no_of_copies']
            try:
                google_books_response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + name)
                google_book_info = google_books_response.json()
                google_book_id = google_book_info['items'][0]["id"]
            except:
                google_book_id = None
            book = Book(name=name, price=price, no_of_copies=no_of_copies, store=store, google_book_id=google_book_id,
                        author=author, user=request.user)
            book.save()
            return HttpResponseRedirect('/store/'+str(store_id)+'/books/')
    else:
        store = get_object_or_404(Store, pk=store_id)
        form = BookForm()
    return render(request, 'books_store/book_create.html', {'form': form, 'store_id':store_id, 'store': store})

def get_books(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    books = Book.objects.all().filter(store=store_id, user=request.user)
    stores = Store.objects.all().filter(user=request.user)
    return render(request, 'books_store/books.html', {'books': books, 'user': request.user, 'store': store, 'stores': stores})

def edit_book(request, store_id, book_id):
    book = get_object_or_404(Book, pk=book_id)
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=book)
        name = form.data['name']
        author = form.data['author']
        price = form.data['price']
        no_of_copies = form.data['no_of_copies']
        book.name = name
        book.author = author
        book.price = price
        book.no_of_copies = no_of_copies
        book.store = store
        book.save()
        return HttpResponseRedirect('/store/'+str(store_id)+'/books/')
    else:
        form = BookForm(instance=book)
    return render(request, 'books_store/book_edit.html', {'form': form, 'book': book, 'store': store})

def delete_book(request, store_id, book_id):
    # store = get_object_or_404(Store, pk=store_id)
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/store/'+str(store_id)+'/books/')

def get_book(request, store_id, book_id):
    store = get_object_or_404(Store, pk=store_id)
    book = get_object_or_404(Book, pk=book_id, user=request.user)
    return render(request, 'books_store/book.html', {'book': book, 'user': request.user, 'store': store})