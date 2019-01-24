from django.contrib import admin
from .models import Question, QuestionChoices, QuestionImage, Quiz, QuizUserContent, QuizScore

from django.contrib import admin
import nested_admin



#FIXME: Search about Overwride default queryset in admin, and customManager()


class QuestionChoicesTabularInline(nested_admin.NestedTabularInline):
    model = QuestionChoices
    extra = 0
    max_num = 4
    min_num = 2



class QuestionTabularInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [QuestionChoicesTabularInline]
    extra = 0
    max_num = 10


class QuestionAdmin(nested_admin.NestedModelAdmin):
    #def get_model_perms(self, request): # hide this model from admin
    #        return {}
    change_list_template = 'admin/change_list_graph.html'
    inlines = [QuestionTabularInline]

class QuestionImageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request): # hide this model from admin
            return {}
    change_list_template = 'admin/change_list_graph.html'


class QuizUserContentAdmin(admin.ModelAdmin):
    model = QuizUserContent
    change_list_template = 'admin/change_list_graph.html'



admin.site.register(QuizUserContent, QuizUserContentAdmin)
admin.site.register(Quiz, QuestionAdmin)
admin.site.register(QuestionImage, QuestionImageAdmin)



admin.site.register(QuizScore)
