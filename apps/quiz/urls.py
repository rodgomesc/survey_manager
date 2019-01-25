from django.urls import include, path

from apps.quiz import views as quiz_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', quiz_views.index),
    path('quiz_view/<int:quiz_id>/', quiz_views.quiz_view, name='quiz-view'),
    path('sucessfull/', TemplateView.as_view(template_name="quiz/sucessfull.html"), name='sucessfull'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
