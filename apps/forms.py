from django import forms
from django.forms import models
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['pdf']
