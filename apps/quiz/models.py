from django.db import models


class QuestionImage(models.Model):
    image = models.FileField(upload_to='img/')


class Question(models.Model):
    name = models.CharField(max_length=70)
    image = models.OneToOneField(QuestionImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question_Choices(models.Model):
    choice = models.CharField(max_length=130)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice


class Quiz(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title


class QuizContent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Question_Choices, on_delete=models.CASCADE)

    def __str__(self):
        return self.quiz.title

