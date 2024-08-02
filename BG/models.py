from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    # comment_set =  => 자동생성
class Q(models.Model):
    제목 = models.CharField(max_length=100)
    보기A = models.CharField(max_length=100)
    보기B = models.CharField(max_length=100)
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Q, on_delete=models.CASCADE) #ForeigKey는 자동으로 부모-자식간 연결할 수 있는 다리를 만들어줌
    # article_id =  => 자동생성
class Q_Comment(models.Model):
    답변 = models.CharField(max_length=100)
    내용 = models.TextField()
    Q_article = models.ForeignKey(Q, on_delete=models.CASCADE)