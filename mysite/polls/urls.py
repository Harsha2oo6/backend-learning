from django.urls import path
from .views import hello_api, question_operations

urlpatterns = [
    path('hello/', hello_api),
    path('questions/', question_operations),
]
