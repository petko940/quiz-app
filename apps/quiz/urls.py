from django.urls import path

from apps.quiz.views import QuizView, ApiView

urlpatterns = [
    path('single-question/', QuizView.as_view(), name='single-question'),
    path('api/<int:pk>/', ApiView.as_view(), name='api-single-question'),
]
