from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200)    #글자 수 제한된 텍스트
    text = models.TextField()                   #글자수 제한 없는 긴 텍스트
    created_date = models.DateTimeField(        #날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  #publish라는 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
