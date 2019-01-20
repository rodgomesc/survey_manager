
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Quiz, Question, QuestionChoices
from django.views import generic
from apps.quiz.templatetags import custom_tags

def index(request, ):
    return render(request, 'quiz/index.html')


class teste(generic.ListView):

    questions = Question.objects.all()
    qs = []
    for question in questions:
        qs.append({
            'question': question.question,
            'choices': [row.choice for row in QuestionChoices.objects.filter(question=question.id)]

        })





def quiz_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions= Question.objects.filter(quiz_id=quiz_id).values('question','id')

    #question_id = Question.objects.get(id=quiz_id).id
    question_list = []
    for question in questions:
        question_list.append({
            'question': question['question'],
            'choices': [row.choice for row in QuestionChoices.objects.filter(question=question['id'])]

        })


    return render(request, 'quiz/index.html', {
        'quiz': quiz,
        'question_list': question_list

    })
