from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from user import models as user_models
from django.conf import settings
from .models import Blog


def homepage(request):
    """
    views to display the homepage fecthing all the blogs from the database model
    """

    # fetch all blog having approve_status as true
    blog_list = Blog.objects.filter(approve_status=True)
    # return user loggeed in details
    user = request.user
    return render(request, "home.html", context={"blog_qset": blog_list, "user": user})


@login_required
def submit_blog(request):
    """
    create a new blog from the form submitted by the user in database model
    """
    if request.method == "POST":
        author = request.user.username
        title = request.POST["title"]
        description = request.POST["desc"]
        content = request.POST["content"]
        category = request.POST["cat"]
        img = request.POST["img"]
        source_link = request.POST["source"]
        Blog.objects.create(
            author=author,
            title=title,
            desc=description,
            blog_content=content,
            thumbnail=img,
            read_more=source_link,
            category=category,
        )
        messages.add_message(request, messages.INFO, "Blog added, waiting for approval")
        return redirect("home")
    return render(request, "addblog.html")


@login_required
def delete_page(request):
    """
    view to render all blogs in admin panel with delete button to delete the blog
    """
    blog_list = Blog.objects.all()
    return render(request, "deletepage.html", context={"blog_qset": blog_list})


@login_required
def delete_blog(request, title):
    """
    view to directly delete the blog from custom admin panel using delete button
    """
    blog = Blog.objects.get(title=title)
    blog.delete()
    messages.add_message(request, messages.INFO, "Blog deleted successfully")
    return redirect("deletepage")


@login_required()
def review_post(request):
    """
    view to review the blog post by admin
    """
    if request.user.is_superuser:
        # fetches all blog post from the database model having approved_status as false
        blog_list = Blog.objects.filter(approve_status=False)
        # fetch logged in User details from the database model
        user = request.user
        return render(
            request, "review.html", context={"blog_qset": blog_list, user: user}
        )
    else:
        messages.add_message(
            request, messages.INFO, "You are not authorized to access this page"
        )
        return redirect("home")


@login_required()
def approve_post(request, title):
    """
    view to approve the blog post by admin
    """
    if request.user.is_superuser:

        blog = Blog.objects.get(title=title)
        blog.approve_status = True
        blog.save()
        messages.add_message(request, messages.INFO, "Blog approved successfully")
        author = blog.author
        # get the user email from the database model
        user = user_models.User.objects.get(username=author)
        mail_address = user.email
        # send mail to mail_address with the subject and message that blog have been approved
        # get current site url
        current_site = request.META['HTTP_HOST']
        message = f"""
        Hi {author}
        Your Blog Post with title "{title}" has been approved by Admin
        here it is, check it out - {current_site}/blogcontent/{title}
        Thank you
        
        """
        send_mail(
            subject="Blog Approved",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail_address],
        )

        return redirect("review_post")
    else:
        messages.add_message(
            request, messages.INFO, "You are not authorized to approve the post"
        )
        return redirect("home")


@login_required()
def decline_post(request, title):
    """
    view to decline the blog post by admin
    """
    if request.user.is_superuser:

        blog = Blog.objects.get(title=title)
        blog.delete()
        messages.add_message(request, messages.INFO, "Blog approved successfully")
        author = blog.author
        # get the user email from the database model
        user = user_models.User.objects.get(username=author)
        mail_address = user.email
        # send mail to mail_address with the subject and message that blog have been approved
        s = send_mail(
            subject="Blog Declined",
            message=f"Your blog '{title}'' has been Declined",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail_address],
        )
        s.send()

        return redirect("review_post")
    else:
        messages.add_message(
            request, messages.INFO, "You are not authorized to approve the post"
        )
        return redirect("home")


@login_required()
def admin(request):
    # if user is admin then only he can access the admin page
    if request.user.is_superuser:
        return render(request, "admin.html")
    else:
        messages.add_message(
            request, messages.INFO, "You are not authorized to access this page"
        )
        return redirect("home")


def blog_content(request, title):
    """
    view to render the blog content of specific blog using it's title in url
    """
    blog = Blog.objects.get(title=title)
    return render(request, "blogdetail.html", context={"blog": blog})


def user_profile(request, username):
    """
    view to render the user profile of specific user using it's username in url
    """
    # only same user can access his profile
    if request.user.username == username:
        user = user_models.User.objects.get(username=username)
        return render(request, "edit_profile.html", context={"user": user})
    else:
        messages.add_message(
            request, messages.INFO, "You cannot view another user profile"
        )
        return redirect("home")


# update user's profile information in database model taking the form data from the user
def update_profile_information(request):
    if request.method == "POST":
        print(request.POST)
        print(request.user.username)
        user = user_models.User.objects.get(username=request.user.username)
        user.username = request.POST["username"]
        try:
            user.profile_pic = request.FILES["profile_pic"]
        except: pass
        user.save()
        messages.add_message(request, messages.INFO, "Profile updated successfully")
        return redirect("home")
    else:
        messages.add_message(
            request, messages.INFO, "You are not authorized to access this page"
        )
        return redirect("home")
