from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from clubs.forms import RegisterForm, CommentForm
from clubs.models import Club, Event, Post, Comment


# Create your views here.
def home(request):
    return render(request, 'clubs/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Успешна регистрация! Моля, влезте в профила си.')
            return redirect('login')

    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'clubs/register.html', context)

def custom_logout_view(request):
    logout(request)
    return redirect('home')

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

class ClubCreateView(LoginRequiredMixin, CreateView):
    model = Club
    fields = ['name', 'description', 'category']
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


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'date', 'location']
    template_name = 'clubs/event_form.html'

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
    template_name = 'clubs/event_detail.html'
    context_object_name = 'event'

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'date', 'location']
    template_name = 'clubs/event_form.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().creator

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'clubs/event_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().creator

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'clubs/post_form.html'

    def form_valid(self, form):
        club = get_object_or_404(Club, pk=self.kwargs['club_id'])
        form.instance.club = club
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.kwargs['club_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club'] = get_object_or_404(Club, pk=self.kwargs['club_id'])
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'clubs/post_form.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'clubs/post_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('club-detail', kwargs={'pk': self.object.club.pk})

    def test_func(self):
        return self.request.user == self.get_object().author


class PostDetailView(DetailView):
    model = Post
    template_name = 'clubs/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_on')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
        return redirect('post-detail', pk=self.object.pk)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'clubs/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = {
            'user': user,
            'clubs': user.created_clubs.all(),
            'events': user.created_events.all(),
            'posts': user.created_posts.all(),
            'comments': user.created_comments.all(),
        }
        return render(request, 'clubs/profile.html', context)


class PublicProfileView(DetailView):
    model = User
    template_name = 'clubs/public_profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['clubs'] = user.created_clubs.all()
        context['events'] = user.created_events.all()
        context['posts'] = user.created_posts.all()
        context['comments'] = user.created_comments.all()
        return context