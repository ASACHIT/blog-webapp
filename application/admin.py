from django.contrib import admin

from user.models import User

from .models import Blog

# Register your models here.
admin.site.register(Blog)
admin.site.register(User)
