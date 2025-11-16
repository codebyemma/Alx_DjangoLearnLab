from django.shortcuts import render
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article, Book
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden, HttpResponse
from django.conf import settings
from .forms import ExampleForm
from .models import Book
from .forms import BookForm, BookSearchForm


def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safe handling (prevents SQL injection)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(),
                "success": True
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@require_http_methods(["GET", "POST"])
def book_list(request):
    """
    List books and provide search.
    Uses BookSearchForm to validate user input; uses ORM filter with parameterization.
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            # Safe: ORM parameterizes the query (no string formatting used)
            books = books.filter(title__icontains=query)

    response = render(request, "bookshelf/book_list.html", {"books": books, "form": form})

    # Optional: add/override CSP header for this response (if you want to set per-view)
    # Only do this when you need per-view customizations (otherwise rely on django-csp)
    # e.g. response["Content-Security-Policy"] = "default-src 'self';"
    return response


@login_required
@permission_required("bookshelf.add_book", raise_exception=True)
def create_book(request):
    """
    Creating a book: uses ModelForm for validation and safe ORM save.
    Protected with permission_required decorator.
    """
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # safe ORM-based creation
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required("bookshelf.change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "bookshelf/form_example.html", {"form": form, "book": book})


@login_required
@permission_required("bookshelf.delete_book", raise_exception=True)
def delete_book(request, pk):
    # Confirmation via GET/POST pattern is recommended
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("bookshelf:book_list")
    return render(request, "bookshelf/confirm_delete.html", {"book": book})




@permission_required('yourapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})


@permission_required('yourapp.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content)
        return redirect("article_list")

    return render(request, "articles/create.html")


@permission_required('yourapp.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("article_list")

    return render(request, "articles/edit.html", {"article": article})


@permission_required('yourapp.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("article_list")

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


def books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/books.html", {"books": books})