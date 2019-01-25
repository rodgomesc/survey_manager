from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from apps.core import views as core_views

urlpatterns = [
    path('', core_views.index),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
