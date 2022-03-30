from django.urls import path
from .views import (
    DeckListView,
    DeckDetailView,
    DeckDeleteView,
    DeckCreateView,
    DeckUpdateView,
)


app_name = 'flash_card'
urlpatterns = [
    path('decks/', DeckListView.as_view(), name='deck-list'),
    path('decks/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('decks/create/', DeckCreateView.as_view(), name='deck-create'),
    path('decks/<int:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('decks/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
]
