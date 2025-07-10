from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView

# from django.views.generic import DetailView

from users.forms import RegisterForm


# Create your views here.

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

class ProfileView(LoginRequiredMixin, TemplateView ):
    template_name = 'clubs/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['clubs'] = user.created_clubs.all()
        context['events'] = user.created_events.all()
        context['posts'] = user.created_posts.all()
        context['comments_count'] = user.created_comments.count()
        return context

# за профили, които се разглеждат от други или място с линкове към тях. и шаблона.
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