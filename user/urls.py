from django.urls import path

from . import views

urlpatterns = [
    path(
        "login", views.login_user, name="login"
    ),  # login url when user is not logged in
    path(
        "logout", views.logout_user, name="logout"
    ),  # logout url when user is logged in
    path(
        "register", views.register_user, name="register"
    ),  # register url when user is not logged in
]
