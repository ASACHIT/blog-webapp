from django.contrib import admin as djadmin
from django.urls import path

from .views import (admin, delete_blog, delete_page, homepage, login_user,
                    logout_user, submit_blog)

urlpatterns = [
    path("djangoadmin", djadmin.site.urls, name="djangoadmin"), # django's default admin panel
    path("admin/", admin, name="admin"),                        # our custom admin panel
    path("", homepage, name="home"),                            # homepage
    path("login", login_user, name="login"),                    # login url when user is not logged in
    path("logout", logout_user, name="logout"),                 # logout url when user is logged in
    path("addblog", submit_blog, name="addblog"),               # url that will be used to add a blog from custom admin panel
    path("deletepage", delete_page, name="deletepage"),         # url that will be used to delete a blof from custom admin panel
    path("delete/<int:pk>", delete_blog, name="delete"),        # url that will be used to delete a blog from custom admin panel
]
