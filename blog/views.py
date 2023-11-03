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

def post_detail(request, post_id):
    print("post_id : ", post_id)

    post = Post.objects.get(id=post_id)
    print("post : ", post)

    context = {
        'post' : post,
    }

    return render(request=request,
                  template_name="post_detail.html",
                  context=context)

# 글/댓글 추가 페이지 기능
def post_add(request):
    return render(request=request,
                  template_name="post_add.html")