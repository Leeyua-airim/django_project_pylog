from django.db import models

# Post 관련 테이블 (포스트)
class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=100)
    content = models.TextField("포스트 내용")

    # 이미지 관련 행
    thumbnail = models.ImageField(verbose_name="썸네일 이미지", # 관리자 페이지에서의 출력이름
                                  upload_to="post", # 업로드된 이미지 파일이 저장될 서브 디렉터리
                                  blank=True) # 비워둘 수 있음

    # Admin 상의 표기
    def __str__(self):
        return self.title

# Comment 모델 생성 (댓글)
class Comment(models.Model):
    # 두 테이블 간의 관계를 설정
    # 연결된 테이블에 Post 객체가 삭제되었을 때 같이 삭제를 의미함
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f'{self.post.title}의 댓글 (ID : {self.id})'