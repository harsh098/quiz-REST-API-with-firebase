from django.urls import path
from . import views

app_name= 'quiz'

urlpatterns = [
    path('', views.QuizView.as_view(), name='quiz'),
    path('r/<str:topic>', views.GetRandomQuestion.as_view(), name='random_fetcher'),
    path('q/<str:topic>', views.GetQuizQuestion.as_view(), name='question_fetcher'),
]