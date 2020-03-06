from django.urls import path
from .views import BooksListView, BooksDetailView, BooksCreatView, BooksUpdateView


urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='books_detail'),
    path('new/', BooksCreatView.as_view(), name='books_new'),
    path('update/<int:pk>/', BooksUpdateView.as_view(), name='books_update')
]