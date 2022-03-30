from django import forms
from .models import Deck, Card


class DeckCreateForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title',
            'icon',
            'description'
        ]
