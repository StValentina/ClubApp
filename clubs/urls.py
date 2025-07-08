from django.urls import path
from . import views
from .views import ClubListView, ClubDetailView, ClubCreateView, ClubUpdateView, ClubDeleteView

urlpatterns = [
    path('clubs/', ClubListView.as_view(), name='club-list'),
    path('clubs/<int:pk>/', ClubDetailView.as_view(), name='club-detail'),
    path('clubs/create/', ClubCreateView.as_view(), name='club-create'),
    path('clubs/<int:pk>/edit/', ClubUpdateView.as_view(), name='club-edit'),
    path('clubs/<int:pk>/delete/', ClubDeleteView.as_view(), name='club-delete'),
]