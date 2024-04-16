from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm, TagForm
from .models import Quote,Author
from django.contrib.auth.decorators import login_required





def main(request):
    return render(request, 'quotesapp/index.html')


@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = AuthorForm()
    return render(request, 'quotesapp/create_author.html', {'form': form})
@login_required
def create_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = QuoteForm()
    return render(request, 'quotesapp/create_quote.html', {'form': form})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = TagForm()
    return render(request, 'quotesapp/tag.html', {'form': form})



def quotes_view(request):
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/quotes.html', {'quotes': quotes})



def authors(request):
    authors = Author.objects.all()
    return render(request, 'quotesapp/authors.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotesapp/author_detail.html', {'author': author})



