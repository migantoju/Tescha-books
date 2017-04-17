from django import forms
from .models import Book

class New_Book_Form(forms.ModelForm):
    title = forms.CharField(label="Titulo", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python For Noobs'}))
    autor = forms.CharField(label="Autor(es)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Guido Van Rossum'}))
    description = forms.CharField(label="Descripcion", min_length=150, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuentanos un poco de que trata... Minimo 150 caracteres'}))
    files = forms.FileField(label="Sube tu archivo", widget=forms.FileInput(attrs={'class': 'file'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coding, Gaming, Eating'}))
    class Meta:
        model = Book
        fields = ('title', 'autor', 'description', 'files', 'book_type', 'tags')
