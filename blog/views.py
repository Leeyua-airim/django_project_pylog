from django.shortcuts import render, redirect
from blog.models import Post, Comment
def post_list(request):
    posts = Post.objects.all() # 모든 포스트

    context = {
        'posts' : posts,
    }

    return render(request=request,
                  template_name="post_list.html",
                  context=context)

# 기능 : 상세 페이지 글 출력
def post_detail(request, post_id):
    print("post_id : ", post_id)

    post = Post.objects.get(id=post_id)
    print("post : ", post)

    if request.method == "POST":
        comment_content = request.POST['comment']
        print("comment_content : ", comment_content)

        Comment.objects.create(
            post=post, # 댓글 생성을 위해서는 포스트가 있어야 한다.
            content=comment_content
        )

    context = {
        'post' : post,
    }

    return render(request=request,
                  template_name="post_detail.html",
                  context=context)

# 글/댓글 추가 페이지 기능
def post_add(request):
    if request.method == "POST":
        print("method POST")
        print(request.FILES)

        title = request.POST['title']
        content = request.POST['content']
        print("title : ", title)
        print("content : ", content)
        # 이미지
        thumbnail = request.FILES['thumbnail']


        # 새로운 컨텐츠 생성
        post = Post.objects.create(title=title,
                                   content=content,
                                   thumbnail=thumbnail,)

        # POST 요청 이후 해당 페이지로 이동
        return redirect(f"/posts/{post.id}")

    else:
        print("method GET")

    return render(request=request,
                  template_name="post_add.html")