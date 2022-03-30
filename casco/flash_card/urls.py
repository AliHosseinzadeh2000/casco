from django.urls import path
from .views import DeckListView


app_name = 'flash_card'

urlpatterns = [
    path('decks/', DeckListView.as_view(), name='deck-list'),
]
