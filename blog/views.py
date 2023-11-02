from django.shortcuts import render
from blog.models import Post
def post_list(request):
    posts = Post.objects.all() # 모든 포스트

    context = {
        'posts' : posts,
    }

    return render(request=request,
                  template_name="post_list.html",
                  context=context)

