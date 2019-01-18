from django.urls import include, path
from .views import index
urlpatterns = [

    path('', index),
    path('nested_admin/', include('nested_admin.urls')),
]
