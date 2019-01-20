from django.urls import include, path

from apps.quiz import views as quiz_views

urlpatterns = [
    path('', quiz_views.index),
    path('quiz_list/<int:quiz_id>/', quiz_views.quiz_list),
    path('test/', quiz_views.teste.as_view())


]
