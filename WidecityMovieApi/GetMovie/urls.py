from django.urls import path
from .views import title
urlpatterns = [
    path('',title.as_view()),
]