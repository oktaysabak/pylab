from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Books'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Authors'
        context['book_list'] = Book.objects.filter(author=context['object'].id)
        return context



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Authors'
        context['books'] = Book.objects.get(author=context['id'])
        
        return context


class BookDetailView(generic.DetailView):
    model = Book



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    books = Book.objects.filter(title__icontains="test")
    genres = Genre.objects.filter(name__icontains="gen")
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'books': books,
        'genres': genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)