from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from apps.statistics import views as statistics_views

urlpatterns = [
    path('', statistics_views.index),
    path('chart_process/', statistics_views.chart_process),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
