from django.contrib import admin
from .models import Post, NeedMember

# Register your models here.
admin.site.register(Post)
admin.site.register(NeedMember)