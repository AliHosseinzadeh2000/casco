from .models import Deck, Card
from django.views.generic import ListView


class DeckListView(ListView):
    template_name = 'deck_list.html'
    queryset = Deck.objects.order_by('-updated_at')
