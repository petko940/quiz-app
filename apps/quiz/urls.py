from django.urls import path

from apps.quiz.api.views import (OneQuestionAPIView,
                                 PythonQuestionsAPIView,
                                 GetRightPythonAnswerAPIView,
                                 SaveQuizResultAPIView,
                                 GetUsernameAPIView,
                                 JSQuestionsAPIView,
                                 GetRightJSAnswerAPIView,
                                 HTMLCSSQuestionsAPIView,
                                 GetRightHTMLCSSAnswerAPIView,
                                 )

from apps.quiz.views import (OneQuestionView,
                             PythonQuizView,
                             JSQuizView,
                             HTMLCSSQuizView,
                             LeaderboardView,
                             RecentQuizzesView,
                             )

urlpatterns = [
    path('single-question/', OneQuestionView.as_view(), name='single-question'),
    path('python-quiz/', PythonQuizView.as_view(), name='python-quiz'),
    path('js-quiz', JSQuizView.as_view(), name='js-quiz'),
    path('html-css-quiz', HTMLCSSQuizView.as_view(), name='html-css-quiz'),

    # leaderboard
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),

    # recent-quizzes
    path('recent-quizzes/', RecentQuizzesView.as_view(), name='recent-quizzes'),

    # apis
    path('api/<int:pk>/', OneQuestionAPIView.as_view(), name='api-single-question'),

    path('api/python-questions/', PythonQuestionsAPIView.as_view(), name='api-python-questions'),
    path('api/python-questions/<int:pk>/', GetRightPythonAnswerAPIView.as_view(), name='api-python-get-right-answer'),

    path('api/js-questions/', JSQuestionsAPIView.as_view(), name='api-js-questions'),
    path('api/js-questions/<int:pk>/', GetRightJSAnswerAPIView.as_view(), name='api-js-get-right-answer'),

    path('api/html-css-questions/', HTMLCSSQuestionsAPIView.as_view(), name='api-html-css-questions'),
    path('api/html-css-questions/<int:pk>/', GetRightHTMLCSSAnswerAPIView.as_view(), name='api-html-css-get-right-answer'),


    path('api/save-quiz-result/', SaveQuizResultAPIView.as_view(), name='api-save-quiz-result'),
    path('api/get-username', GetUsernameAPIView.as_view(), name='api-get-username'),

]
