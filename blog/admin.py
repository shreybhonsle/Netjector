from django.contrib import admin
from blog.models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Featured)
admin.site.register(blogcomment)