from django.urls import path
from .views import title
urlpatterns = [
    path('<str:title>',title.as_view()),
]