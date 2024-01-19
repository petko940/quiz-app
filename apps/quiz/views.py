import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic as views
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.quiz.models import Questions
from apps.quiz.serializers import QuestionSerializer


# Create your views here.
class QuizView(views.TemplateView):
    template_name = 'quiz/single-question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = random.choice(Questions.objects.all())
        return context


class ApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            question = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            question = None

        if question:
            serializer = QuestionSerializer(question)
            return Response(serializer.data)

        return Response()
