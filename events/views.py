from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from clubs.models import Club
from events.models import Event


# Create your views here.
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'date', 'location']
    template_name = 'events/event_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = get_object_or_404(Club, pk=self.kwargs['club_id'])
        return context

    def form_valid(self, form):
        club = get_object_or_404(Club, pk=self.kwargs['club_id'])
        form.instance.club = club
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.kwargs['club_id']})

class EventDetailView(DeleteView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'date', 'location']
    template_name = 'events/event_form.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().creator

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().creator
