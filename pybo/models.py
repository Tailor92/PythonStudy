from django.db import models

# Create your models here.

# models 작성
class Question(models.Model):
    # 질문 제목 최대 200자
    subject = models.CharField(max_length=200)
    # 질문 내용
    content = models.TextField()
    # 질문 작성 일시
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 질문과 매핑 질문 삭제시 해당 답변 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변 내용
    content = models.TextField()
    # 답변 작성 일시
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content