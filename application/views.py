from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Blog

def homepage(request):
    """
    views to display the homepage fecthing all the blogs from the database model
    """
    blog_list = Blog.objects.all()  # fetching all the blogs from the database model
    return render(request, "home.html", context={"blog_qset": blog_list})



# decorator to check if the user is logged in or not, if not redirect to login page then further process..
@login_required  
def submit_blog(request):
    """
    create a new blog from the form submitted by the user in database model
    """
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["desc"]
        category = request.POST["cat"]
        img = request.POST["img"]
        source_link = request.POST["source"]
        s = Blog.objects.create(
            title=title,
            desc=description,
            thumbnail=img,
            read_more=source_link,
            category=category,
        )
        messages.add_message(request, messages.INFO, f"{title} added successfully")
        return redirect("home")
    return render(request, "addblog.html")


def login_user(request):
    """
    views to login the user taking input from login.html form and authenticating the user
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(
                request, messages.INFO, f"{username} Logged in successfully"
            )
            return redirect("admin")
        else:
            messages.add_message(request, messages.INFO, "Invalid Credentials")
            return redirect("login")
    return render(request, "login.html")


@login_required
def delete_page(request):
    """
    view to render all blogs in admin panel with delete button to delete the blog
    """
    blog_list = Blog.objects.all()
    return render(request, "deletepage.html", context={"blog_qset": blog_list})


@login_required()
def delete_blog(request, pk):
    """
    view to directly delete the blog from custom admin panel using delete button
    """
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    messages.add_message(request, messages.INFO, "Blog deleted successfully")
    return redirect("deletepage")


@login_required
def admin(request):
    return render(request, "admin.html")


def logout_user(request):
    """
    views to logout the logged in user
    """
    logout(request)
    messages.add_message(request, messages.INFO, "Logged out successfully")
    return redirect("home")
