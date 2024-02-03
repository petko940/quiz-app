import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.quiz.models import (PythonQuestions,
                              JSQuestions,
                              HTMLCSSQuestions,
                              QuizResult
                              )

from apps.quiz.api.serializers import (SingleQuestionSerializer,
                                       PythonQuestionsSerializer,
                                       GetRightPythonAnswerSerializer,
                                       QuizResultSerializer,
                                       JSQuestionsSerializer,
                                       GetRightJSAnswerSerializer,
                                       HTMLCSSQuestionsSerializer,
                                       GetRightHTMLCSSAnswerSerializer)
from apps.quiz.permissions import JsTokenPermission


class OneQuestionAPIView(APIView):
    permission_classes = [JsTokenPermission]

    def get(self, request, pk, *args, **kwargs):
        try:
            # TODO: add dbs
            question = PythonQuestions.objects.get(pk=pk)
        except PythonQuestions.DoesNotExist:
            question = None

        if question:
            serializer = SingleQuestionSerializer(question)
            return Response(serializer.data)

        return Response()


class BaseQuestionAPIView(APIView):
    permission_classes = [JsTokenPermission]
    model = None  # To be defined in subclasses

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)


# python
class PythonQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        count = 1
        questions = set(random.sample(list(PythonQuestions.objects.all()), count))
        serializer = PythonQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class GetRightPythonAnswerAPIView(BaseQuestionAPIView):
    model = PythonQuestions

    def get(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        serializer = GetRightPythonAnswerSerializer(question)
        return Response(serializer.data, status=200)


# Javascript
class JSQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        count = 1
        questions = set(random.sample(list(JSQuestions.objects.all()), count))
        serializer = JSQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class GetRightJSAnswerAPIView(BaseQuestionAPIView):
    model = JSQuestions

    def get(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        serializer = GetRightJSAnswerSerializer(question)
        return Response(serializer.data, status=200)


# HTML CSS
class HTMLCSSQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        count = 1
        questions = set(random.sample(list(HTMLCSSQuestions.objects.all()), count))
        serializer = HTMLCSSQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class GetRightHTMLCSSAnswerAPIView(BaseQuestionAPIView):
    model = HTMLCSSQuestions

    def get(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        serializer = GetRightHTMLCSSAnswerSerializer(question)
        return Response(serializer.data, status=200)


class SaveQuizResultAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            correct_answers = int(request.data.get('correct_answers', 0))
            finish_time = int(request.data.get('finish_time', 0))
            quiz_name = request.data.get('quiz_name', '')
            name = {
                'python-quiz': 'Python',
                'js-quiz': 'JavaScript',
                'html-css-quiz': 'HTML/CSS',
            }
            quiz_name = name[quiz_name]

            result = QuizResult.objects.create(
                user=user,
                correct_answers=correct_answers,
                finish_time=finish_time,
                quiz_name=quiz_name,
            )

            serializer = QuizResultSerializer(result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetUsernameAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'username': request.user.username})
