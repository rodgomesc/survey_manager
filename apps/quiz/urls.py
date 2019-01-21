from django.urls import include, path

from apps.quiz import views as quiz_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', quiz_views.index),
    path('quiz_view/<int:quiz_id>/', quiz_views.QuizView.as_view(), name='quiz-view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
