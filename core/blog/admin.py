from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostCustomAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status','created_date', 'published_data']
    list_filter = ['status', 'category', 'published_data']
    search_fields = ['title', 'content']

admin.site.register(Post)
admin.site.register(Category)
