from django.db import models
from django.utils import timezone


class Post(models.Model):
    #table을 만드는 과정,'post'가 데이터베이스가 저장된다고 하면 된다
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #글자수가 제한된 텍스트를 정의할 때, 사용한다.
    text = models.TextField()
    #글자수가 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
            default=timezone.now)
    # 글자수에 제한이 없는 긴 텍스트를 위한 속성(블로그 컨텐츠)
    # 만들어지는 순간의 시간
    published_date = models.DateTimeField(
            blank=True, null=True)
    # publish라고 선언했을때의 시간

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #__str__ 메서드를 호출하면, return self.title
