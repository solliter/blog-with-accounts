from django.contrib import admin
from .models import Blog

admin.site.register(Blog)
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fields = ['blog_title', 'blog_text', 'blog_date']
    list_filter = ['blog_date']

