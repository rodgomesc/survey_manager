from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=70)

class QuizContent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)

class Question(models.Model):
    name = models.CharField(max_length=70)

class QuestionImage(models.Model):
    image = models.FileField(upload_to='img/')
    question = models.OneToOneField(Question, on_delete=models.PROTECT)


