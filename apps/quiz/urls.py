from django.urls import path

from apps.quiz.views import QuizView, ApiView

urlpatterns = [
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('api/<int:pk>/', ApiView.as_view(), name='api-quiz'),
]
