from django.urls import path
from .views import hello_api, get_questions, create_question

urlpatterns = [
    path('hello/', hello_api),
    path('questions/', get_questions),
    path('questions/create/', create_question),
]
