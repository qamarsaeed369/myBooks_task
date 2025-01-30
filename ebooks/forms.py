from django import forms
from .models import myBooks

class EbookForm(forms.ModelForm):
    class Meta:
        model = myBooks
        fields = ['title', 'author', 'description', 'published_date']
