from django import forms

from posts.models import Comment, Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'row': 3}),
        }
