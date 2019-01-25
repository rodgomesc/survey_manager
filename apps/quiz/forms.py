from django import  forms
from .models import QuestionChoices, QuizUserContent


#TODO: I think the best way to implement this is using formsets but if I get stuck on it I will not have time to finish
# the project, I hope it's enough Guys!
class QuizUserContentForm(forms.Form):


    def __init__(self,  questions, *args, **kwargs):
        super(QuizUserContentForm, self).__init__(*args, **kwargs)
        self.questions = questions

        for question in questions:
            choices = []
            for answer in question.questionchoices_set.all():
                choices.append((answer.pk, answer.choice,))

            self.fields['{0}'.format(question.pk)] = \
                forms.ChoiceField(label=question,
                                  choices=choices, widget=forms.RadioSelect)
