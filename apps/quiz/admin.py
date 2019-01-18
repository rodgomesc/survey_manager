from django.contrib import admin
from .models import Question, QuestionChoices, QuestionImage, Quiz

from django.contrib import admin
import nested_admin


class QuestionChoicesTabularInline(nested_admin.NestedTabularInline):
    model = QuestionChoices
    extra = 1


class QuestionTabularInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [QuestionChoicesTabularInline]
    extra = 1


class QuizAdmin(nested_admin.NestedModelAdmin):
   inlines = [QuestionTabularInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuestionImage)