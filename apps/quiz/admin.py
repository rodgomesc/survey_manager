from django.contrib import admin
from .models import Question, QuestionChoices

from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class QuestionTabularInline(NestedTabularInline):
    model = Question
    extra = 1

class QuestionAdmin(NestedModelAdmin):
   inlines = [QuestionTabularInline]

admin.site.register(Question, QuestionTabularInline)