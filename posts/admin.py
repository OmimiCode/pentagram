from django.contrib import admin
from .models import *


# Register your models here.


class OwnerPost(admin.ModelAdmin):
    list_display = ( 'image', 'description')


admin.site.register(Post, OwnerPost)

admin.site.register(Comment)
