from django.urls import path
from .views import *

urlpatterns = [
    path('', QuizHome.as_view(), name='home'),
    path('quiz/<slug:test_slug>', show_quiz, name='quiz'),
    path('quiz/result', show_quiz, name='result'),
    path('about', about, name='about'),
]
