from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail']
    # admin 페이지에 보여주는 디스플레이 값

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass