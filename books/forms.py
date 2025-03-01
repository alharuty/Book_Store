from django import forms
from .models import Book

class formBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publish_date', 'isbn']