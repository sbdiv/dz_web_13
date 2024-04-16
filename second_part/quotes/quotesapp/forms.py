from django import forms
from .models import Author, Quote, Tag

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['tags', 'author', 'quote']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
