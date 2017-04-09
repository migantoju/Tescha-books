from django import forms
from .models import Book

class New_Book_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    autor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files = forms.FileField(widget=forms.ClearableFileInput())
    class Meta:
        model = Book
        fields = ('title', 'autor', 'description', 'files', 'book_type')
