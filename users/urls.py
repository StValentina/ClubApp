from django import views
from django.urls import path

from users.views import ProfileView, PublicProfileView

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/<int:pk>/', PublicProfileView.as_view(), name='user-profile'),

]