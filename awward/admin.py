from django.contrib import admin
from .models import Post
admin.site.site_header='Shaz Developer'

# Register your models here.
admin.site.register(Post)
