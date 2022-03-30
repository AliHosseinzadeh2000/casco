from .models import Deck, Card
from django.views.generic import ListView, DetailView


class DeckListView(ListView):
    template_name = 'deck_list.html'
    queryset = Deck.objects.order_by('-updated_at')


class DeckDetailView(DetailView):
    template_name = 'deck_detail.html'
    model = Deck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d1 = Deck.objects.get(pk=self.kwargs.get('pk')) 
        context['card_list'] = d1.card_set.all()
        return context

    def get_object(self):
        deck = super().get_object()
        deck.views_count += 1
        deck.save()
        return deck
