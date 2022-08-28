from rest_framework import generics,status
from .models import Quiz,Question
from .serializers import QuestionSerializer, QuizSerializer, RandomQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from core.exceptions import InvalidAuthToken
from core.auth import FirebaseAuthentication
# Create your views here.

class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class GetRandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        user = FirebaseAuthentication.authenticate(request)[0]
        if user:
            question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1] 
            serializer = RandomQuestionSerializer(question, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"Forbidden 403"},status=status.HTTP_403_FORBIDDEN)
    
            

class GetQuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        user = FirebaseAuthentication.authenticate(request)[0]
        if user:
            quiz_questions=Question.objects.filter(quiz__title=kwargs['topic'])
            serializer = QuestionSerializer(quiz_questions, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"Forbidden 403"},status=status.HTTP_403_FORBIDDEN)