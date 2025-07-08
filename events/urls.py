from django.urls import path

from events.views import EventDetailView, EventUpdateView, EventDeleteView, EventCreateView

urlpatterns = [
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('clubs/<int:club_id>/events/create/', EventCreateView.as_view(), name='event-create'),
]