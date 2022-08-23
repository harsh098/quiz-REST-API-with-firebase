from rest_framework import serializers
from .models import Quiz, Question, Answer

class QuizSerializer(serializers.ModelSerializer):
    #Serialize quiz Data
     class Meta:
         model = Quiz
         fields = [
             'title',
         ]
class AnswerSerializer(serializers.ModelSerializer):
    #Serialize Answers Data
    class Meta:
        model = Answer
        fields =[
            'id',
            'ans_text',
            'is_right',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    #Serialize Question w/ Quiz Data
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    class Meta:
        model = Question
        fields = [
            'quiz',
            'title', 
            'answer',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    #to serialize fetched questions reagardless of quiz
    answer =  AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields =[
            'title',
            'answer',
        ]
