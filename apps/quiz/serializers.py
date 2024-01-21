from rest_framework import serializers
from .models import PythonQuestions


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        fields = 'correct_option',
