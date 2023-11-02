from django.contrib import admin
from django.urls import path
from config.views import index
from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list)
]

