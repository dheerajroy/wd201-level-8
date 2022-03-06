from django.urls import path
from .views import UserLoginView, UserSignupView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/", UserSignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
]