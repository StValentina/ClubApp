from django.urls import path

from events.views import EventDetailView, EventUpdateView, EventDeleteView, EventCreateView

urlpatterns = [
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('create/<int:club_id>/', EventCreateView.as_view(), name='event-create'),
]