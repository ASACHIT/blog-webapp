from django.contrib import admin as djadmin
from django.urls import include, path

urlpatterns = [
    # path(
    #     "djangoadmin", djadmin.site.urls, name="djangoadmin"
    # ),  # django's default admin panel
    path("", include("application.urls"), name="homepage"),
    path("verification/", include("verify_email.urls")),
    path("user/", include("user.urls")),
]
