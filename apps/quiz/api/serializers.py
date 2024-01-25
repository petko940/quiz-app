from rest_framework import serializers

from apps.quiz.models import PythonQuestions, QuizResult


class SingleQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        fields = 'correct_option',


class PythonQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        exclude = 'correct_option',


class GetRightAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        fields = 'correct_option',


class PythonQuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = '__all__'
