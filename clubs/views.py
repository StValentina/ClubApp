from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from clubs.models import Club
from events.models import Event
from posts.models import Post


# Create your views here.
def home(request):
    return render(request, 'common/home.html')

class ClubListView(ListView):
    model = Club
    template_name = 'clubs/club_list.html'
    context_object_name = 'clubs'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(category__icontains=q) |
                Q(creator__username__icontains=q)
            )

        if category and category != 'всички':
            queryset = queryset.filter(category__icontains=category)

        return queryset


class ClubDetailView(DetailView):
    model = Club
    template_name = 'clubs/club_detail.html'
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(club=self.object).order_by('-date')
        context['posts'] = Post.objects.filter(club=self.object)
        return context

class ClubCreateView(LoginRequiredMixin, CreateView):
    model = Club
    fields = ['name', 'description', 'image_url', 'category']
    template_name = 'clubs/club_form.html'
    success_url = reverse_lazy('club-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ClubUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Club
    fields = ['name', 'description', 'category']
    template_name = 'clubs/club_form.html'
    success_url = reverse_lazy('club-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        club = self.get_object()
        return self.request.user == club.creator

class ClubDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Club
    template_name = 'clubs/club_confirm_delete.html'
    success_url = reverse_lazy('club-list')

    def test_func(self):
        club = self.get_object()
        return self.request.user == club.creator




