from django.urls import path

from clubs.views import PostCreateView
from posts.views import PostUpdateView, PostDeleteView, PostDetailView, CommentDeleteView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/<int:club_id>/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]