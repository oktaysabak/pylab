from django.urls import include
from django.urls import path
from .views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    #path('catalog/', include('catalog.urls')),
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
]