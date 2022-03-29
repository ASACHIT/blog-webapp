from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin as djadmin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),  # homepage
    path("admin/", views.admin, name="admin"),  # our custom admin panel
    path(
        "djangoadmin", djadmin.site.urls, name="djangoadmin"
    ),  # django's default admin panel
    path(
        "addblog", views.submit_blog, name="addblog"
    ),  # url that will be used to add a blog from custom admin panel
    path(
        "deletepage", views.delete_page, name="deletepage"
    ),  # url that will be used to delete a blof from custom admin panel
    path(
        "delete/<str:title>", views.delete_blog, name="delete"
    ),  # url that will be used to delete a blog from custom admin panel
    path(
        "blogcontent/<str:title>", views.blog_content, name="blogcontent"
    ),  # url that will be used to display the blog content
    path(
        "approve_post/<str:title>", views.approve_post, name="approve_post"
    ),  # url that will be used to approve the blog
    path(
        "decline_post/<str:title>", views.decline_post, name="decline_post"
    ),  # url that will be used to decline the blog
    path(
        "review_post/", views.review_post, name="review_post"
    ),  # url that will be used to review the blog
    path(
        "user_profile/<str:username>", views.user_profile, name="user_profile"
    ),  # url that will be used to edit the profile
    path(
        "update_profile_information/",
        views.update_profile_information,
        name="update_profile_information",
    ),  # url that will be used to update the profile
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
