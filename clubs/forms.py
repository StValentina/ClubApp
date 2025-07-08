from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from clubs.models import Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'row': 3}),
        }

