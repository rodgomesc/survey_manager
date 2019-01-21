
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Quiz, Question, QuestionChoices, QuestionImage
from django.views.generic import (
        DetailView
        )
from apps.quiz.templatetags import custom_tags

def index(request, ):
    return render(request, 'quiz/index.html')


class QuizView(DetailView):
    template_name = 'quiz/index.html'

    def get_object(self):
        quiz_id = self.kwargs.get("quiz_id")
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        questions = Question.objects.filter(quiz_id=quiz_id).values('question','id')
        question_list = []

        def image_exist(object):
            if object.image is not None:
                return object.image.image.url
            else:
                return '/img/default.jpeg'

        for question in questions:

           question_list.append({
               'question': question['question'],
               'question_image': image_exist(Question.objects.get(pk=question['id'])) ,#'#Question.objects.get(pk=question['id']).image if Question.objects.filter(pk=question['id']).values('image').exists() else '',#if image_url is not None else 'img/default.jpg',
               'choices': [row.choice for row in QuestionChoices.objects.filter(question=question['id'])]

           })
        context = {
            'quiz': quiz,
            'question_list': question_list
        }
        return context
