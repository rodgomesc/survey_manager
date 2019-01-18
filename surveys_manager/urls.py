from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.quiz.urls')),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),

]
