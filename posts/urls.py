from django.urls import path

from clubs.views import PostCreateView
from posts.views import PostUpdateView, PostDeleteView, PostDetailView, CommentDeleteView

urlpatterns = [
    path('clubs/<int:club_id>/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]