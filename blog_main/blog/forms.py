from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'email': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'Tu email'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows':5,
                'placeholder': 'Escribe tu comentario'
            }),
        }