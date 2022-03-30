from .models import Deck, Card
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import DeckCreateForm


class DeckCreateView(SuccessMessageMixin, CreateView):
    template_name = 'deck_create.html'
    form_class = DeckCreateForm
    success_url = reverse_lazy('flash_card:deck-list')

    success_message = '"%(title)s" was created successfully.'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )


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


class DeckDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'deck_delete.html'
    model = Deck
    success_url = reverse_lazy('flash_card:deck-list')

    success_message = '"%(title)s" was deleted successfully.'
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )
