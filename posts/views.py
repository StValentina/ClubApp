from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView

from clubs.forms import CommentForm
from posts.models import Post, Comment


# Create your views here.
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