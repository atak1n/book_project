from django.urls import path
from .views import BooksListView, BooksDetailView, BooksCreatView


urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='books_detail'),
    path('new/', BooksCreatView.as_view(), name='books_new')
]