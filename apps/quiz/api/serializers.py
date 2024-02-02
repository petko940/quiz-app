import random

from rest_framework import serializers
from apps.quiz.models import PythonQuestions, QuizResult, JSQuestions, HTMLCSSQuestions


class SingleQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        random_model = random.choice([JSQuestions])
        model = random_model
        fields = 'correct_option',


# python
class PythonQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        exclude = 'correct_option',


class GetRightPythonAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        fields = 'correct_option',


# --------

# JavaScript
class JSQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSQuestions
        exclude = 'correct_option',


class GetRightJSAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSQuestions
        fields = 'correct_option',


# --------

# HTML and CSS
class HTMLCSSQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTMLCSSQuestions
        exclude = 'correct_option',


class GetRightHTMLCSSAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTMLCSSQuestions
        fields = 'correct_option',


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = '__all__'
