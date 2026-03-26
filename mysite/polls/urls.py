from django.urls import path
from .views import hello_api, question_operations, get_answers

urlpatterns = [
    path('hello/', hello_api),
    path('questions/', question_operations),
    path("questions/<int:question_id>/answers", get_answers),
]
