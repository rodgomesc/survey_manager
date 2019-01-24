from django.contrib import admin
from django.urls import include, path
import debug_toolbar
urlpatterns = [
    path('', include('apps.quiz.urls')),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('__debug__/', include(debug_toolbar.urls)),


]
