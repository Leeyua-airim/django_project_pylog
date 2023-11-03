from django.contrib import admin
from django.urls import path
from config.views import index
from blog.views import post_list,post_detail, post_add

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail), # 자동생성되어 있는 row(post_id)
    path('posts/add/', post_add)
]

# static() 함수를 사용하여 정적파일에 대한 URL 패턴을 추가하는 방식
# http://127.0.0.1:8000/media/post/스크린샷_2023-11-02_오전_10.21.05.png
urlpatterns += static(
    # URL 의 접두어가 MEDIA_URL 일 때는 정적파일을 돌려준다.
    # MEDIA_URL = 'media/'
    # MEDIA_ROOT = BASE_DIR / "media" # 이 하단에 이미지 관련 디렉터리
    prefix        = settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)

print("urlpatterns : ", urlpatterns)