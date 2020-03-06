from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'all_books'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'books_detail.html'
    context_object_name = 'book'


class BooksCreatView(CreateView):
    model = Book
    template_name = 'books_new.html'
    fields = ['title', 'year', 'author', 'price']


class BooksUpdateView(UpdateView):
    model = Book
    template_name = 'books_update.html'
    fields = ['title', 'year', 'author', 'price']



class BooksDeleteView(DeleteView):
    model = Book
    template_name = 'books_delete.html'
    success_url = 'home.html'
