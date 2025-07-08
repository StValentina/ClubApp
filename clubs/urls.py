from django.urls import path
from . import views
from .views import ClubListView, ClubDetailView, ClubCreateView, ClubUpdateView, ClubDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('clubs/', ClubListView.as_view(), name='club-list'),
    path('register', views.register, name='register'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),
    path('clubs/create/', ClubCreateView.as_view(), name='club-create'),
    path('clubs/<int:pk>/edit/', ClubUpdateView.as_view(), name='club-edit'),
    path('clubs/<int:pk>/delete/', ClubDeleteView.as_view(), name='club-delete'),
    path('clubs/<int:club_id>/events/create/', views.EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDeleteView.as_view(), name='event-delete'),
    path('clubs/<int:club_id>/posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('users/<int:pk>/', views.PublicProfileView.as_view(), name='user-profile'),
]