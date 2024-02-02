import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic as views

from apps.quiz.mixins import LogoutRequiredMixin
from apps.quiz.models import (PythonQuestions,
                              JSQuestions,
                              QuizResult,
                              HTMLCSSQuestions
                              )


# Create your views here.
class QuizView(LogoutRequiredMixin, views.TemplateView):
    template_name = 'quiz/single-question.html'

    @staticmethod
    def get_question_model():
        question_models = [PythonQuestions, JSQuestions, HTMLCSSQuestions]
        return random.choice(question_models)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['question'] = random.choice(PythonQuestions.objects.all())
        question_model = self.get_question_model()

        context['question'] = random.choice(question_model.objects.all())
        return context


class PythonQuizView(LoginRequiredMixin, views.TemplateView):
    template_name = 'quiz/python-quiz.html'
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = PythonQuestions.objects.all()
        return context


class JSQuizView(LoginRequiredMixin, views.TemplateView):
    template_name = 'quiz/js-quiz.html'
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = JSQuestions.objects.all()
        return context


class HTMLCSSQuizView(LoginRequiredMixin, views.TemplateView):
    template_name = 'quiz/html-css-quiz.html'
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = HTMLCSSQuestions.objects.all()
        return context


class LeaderboardView(views.TemplateView):
    template_name = 'quiz/leaderboard.html'
    queryset = QuizResult.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Python
        sorted_by_correct_answers_python = (self.queryset.filter(quiz_name='Python', correct_answers__gt=0)
                                            .order_by('-correct_answers', 'finish_time'))

        page_python = self.request.GET.get('page_python', 1)
        paginator_python = Paginator(sorted_by_correct_answers_python, self.paginate_by)

        try:
            python_leaderboard = paginator_python.page(page_python)
        except PageNotAnInteger:
            python_leaderboard = paginator_python.page(1)
        except EmptyPage:
            python_leaderboard = paginator_python.page(paginator_python.num_pages)

        context['python_leaderboard'] = python_leaderboard

        # JavaScript
        sorted_by_correct_answers_js = (self.queryset.filter(quiz_name='Js', correct_answers__gt=0)
                                        .order_by('-correct_answers', 'finish_time'))

        page_js = self.request.GET.get('page_js', 1)
        paginator_js = Paginator(sorted_by_correct_answers_js, self.paginate_by)

        try:
            js_leaderboard = paginator_js.page(page_js)
        except PageNotAnInteger:
            js_leaderboard = paginator_js.page(1)
        except EmptyPage:
            js_leaderboard = paginator_js.page(paginator_js.num_pages)

        context['javascript_leaderboard'] = js_leaderboard

        # TODO HTML/CSS
        return context


class RecentQuizzesView(views.TemplateView):
    template_name = 'quiz/recent-quizzes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if len(QuizResult.objects.all()) <= 10:
            context['recent_quizzes'] = QuizResult.objects.all().order_by('-id')
        else:
            context['all_quizzes'] = QuizResult.objects.all().count()
            context['recent_quizzes'] = QuizResult.objects.all().order_by('-id')[:10]

        return context
