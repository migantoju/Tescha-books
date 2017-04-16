from django import forms
from .models import Book

class New_Book_Form(forms.ModelForm):
    title = forms.CharField(label="Titulo", widget=forms.TextInput(attrs={'class': 'form-control'}))
    autor = forms.CharField(label="Autor(es)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Cuentanos un poco de que trata...", min_length=150, widget=forms.Textarea(attrs={'class': 'form-control'}))
    files = forms.FileField(label="Sube tu archivo", widget=forms.FileInput(attrs={'class': 'file'}))

    class Meta:
        model = Book
        fields = ('title', 'autor', 'description', 'files', 'book_type', 'tags')
