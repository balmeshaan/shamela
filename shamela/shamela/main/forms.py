from django import forms
from .models import UserBooks


class BookForm(forms.ModelForm):
    class Meta:
        model = UserBooks
        fields = ('name', 'description', 'book_file')