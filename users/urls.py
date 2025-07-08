from django.urls import path
from users import views
from users.views import ProfileView, PublicProfileView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/', PublicProfileView.as_view(), name='user-profile'),
]