from django.urls import path
from .views import register_user, login_user, user_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', user_profile, name='profile'),
]

