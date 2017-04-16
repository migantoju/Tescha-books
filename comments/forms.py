from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    text = forms.CharField(label="Comentario:", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('text', )
