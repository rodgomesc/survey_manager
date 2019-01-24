
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (
        Quiz, Question,
        QuizUserContent,
        QuizScore,
        )


from .forms import QuizUserContentForm

from django.views.generic.edit import (
        FormView
        )

def index(request, ):

    return render(request, 'quiz/index.html')


class QuizView(FormView):
    template_name = 'quiz/index.html'
    form_class = QuizUserContent
    success_url = '/thanks/'

    def get(self, request, *args, **kwargs):

        quiz = get_object_or_404(Quiz, pk=self.kwargs['quiz_id'])
        form = QuizUserContentForm(questions=quiz.question_set.all())

        if request.method == "POST":
            for key, value in request.POST.items():
                # we dont want to store then token
                if key != 'csrfmiddlewaretoken':
                    # key is pk of Question, value is pk of choice
                    p = QuizUserContent(quiz_id=self.kwargs['quiz_id'], question_id=key,  choice_id=value)
                    p.save()
            #store score for report
            QuizScore(quiz_id = self.kwargs['quiz_id']).save()

            #times that people answered the quiz_id=1
            #vote_count = QuizScore.objects.filter(quiz_id=1).count()
            #print(vote_count)


        # this will allow to find the corresponding image for each question with filter get_image_from_question
        form_id_list = Question.objects.filter(quiz_id=self.kwargs['quiz_id']).values_list('id', flat=True)
        obj_list = zip(form, form_id_list) # later.... {% for form, question_id in obj_list %}...
        context = {
            'obj_list': obj_list,
            'quiz': quiz.title,
            }

        return render(request, self.template_name, context)

