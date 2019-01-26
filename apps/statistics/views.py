from django.http import HttpResponse
from django.shortcuts import render
from apps.quiz.models import *
import json
from django.http import JsonResponse

# is receive ajax request with a id, and return data in c3chart format
def chart_process(request):

    if request.method == "GET":

        return HttpResponse(json.dumps({"msg": "incorrect request"}),
                            content_type="application/json")

    elif request.method == "POST":

        quiz_id = request.POST.get('quiz_id')
        quiz = Quiz.objects.get(id=quiz_id)
        votes = quiz.quizusercontent_set.select_related()
        choice_counts = {}


        for vote in votes:
            if vote.choice.id not in choice_counts:
                choice_counts[vote.choice.id] = {
                    'item': vote.choice.choice,
                    'count': 0
                }
            choice_counts[vote.choice.id]['count'] += 1

        dict_list = []
        last = []

        # returned data needs to be in c3chart format [['name',value], ['name', value]]
        for i, j in choice_counts.items():
            dict_list.append(j)
        for i in dict_list:
           last.append(list((i['item'], i['count'])))

        return JsonResponse({'data': last, }, safe=False,  json_dumps_params={'ensure_ascii':False})

    else:
        return HttpResponse(json.dumps({"msg": "incorrect request"}),
                            content_type="application/json")


def index(request):


    quizzes = Quiz.objects.all()
    object_list = []
    for quiz in quizzes:

        object_list.append({
            'quiz':quiz,
            'question_number': Question.objects.filter(quiz_id=quiz.id).count(),
            'score': QuizScore.objects.filter(quiz_id=quiz.id).count(),
            'questions': Question.objects.filter(quiz_id=quiz.id),
        })

    return render(request, 'statistics/index.html', {'object_list': object_list})
