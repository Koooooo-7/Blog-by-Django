from django.contrib import admin

# Register your models here.
from .models import User, Category, Tags, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'excerpt']


# 注册模型
admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tags)
