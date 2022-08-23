from rest_framework import generics
from .models import Quiz,Question
from .serializers import QuestionSerializer, QuizSerializer, RandomQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class GetRandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1] 
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class GetQuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz_questions=Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz_questions, many=True)
        return Response(serializer.data)
