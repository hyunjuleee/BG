from django.db import models

# Create your models here.
class Q(models.Model):
    제목 = models.CharField(max_length=100)
    보기A = models.CharField(max_length=100)
    보기B = models.CharField(max_length=100)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Q, on_delete=models.CASCADE)