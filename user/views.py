from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from verify_email.email_handler import send_verification_email

from .forms import UserForm


def login_user(request):
    """
    views to login the user taking input from login.html form and authenticating the user
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(
                request, messages.INFO, f"{user.username} logged in successfully"
            )
            return redirect("home")
        else:
            messages.add_message(request, messages.INFO, "Invalid Credentials")
            return redirect("login")
    return render(request, "login.html")


def logout_user(request):
    """
    views to logout the logged in user
    """
    logout(request)
    messages.add_message(request, messages.INFO, "Logged out successfully")
    return redirect("home")


def register_user(request):
    """
    views to register user with name email password
    """
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            # send activation link to user
            inactive_user = send_verification_email(request, form)
            messages.add_message(
                request,
                messages.INFO,
                f"{inactive_user.username} registered | activation link sent to your mail",
            )
        else:
            print(form.errors)
            messages.add_message(
                request,
                messages.INFO,
                "ERROR",
            )
            return render(request, "register.html", {"form": form})

    return render(request, "register.html")
