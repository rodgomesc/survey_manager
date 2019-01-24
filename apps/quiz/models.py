from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title

#every time a Quiz is answered an entry is generated in this table
class QuizScore(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class QuestionImage(models.Model):
    description = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.description

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=70)
    image = models.ForeignKey(QuestionImage, on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return self.question

class QuestionChoices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=130)
    def __str__(self):
        return '{0}'.format(self.choice)


class QuizUserContent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(QuestionChoices, on_delete=models.CASCADE)


    def __str__(self):
        return self.quiz.title
