from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural =  'Quizzes'
        ordering = ['id']


class UpdateModel(models.Model):
    date_updated =  models.DateTimeField(verbose_name="Last Updated", auto_now=True)

    class Meta:
        abstract = True


class Question(UpdateModel):
    DIFF_SCALE = (
        (0,'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    )

    TYPE = (
        (0 ,'Multiple Choice'),
    )

    quiz = models.ForeignKey(Quiz, related_name='question',  on_delete=models.CASCADE)
    type = models.IntegerField(default=0, choices=TYPE, verbose_name = 'Question Type')
    difficulty_level = models.IntegerField(default=0, choices=DIFF_SCALE,  verbose_name=  'Difficulty Level')
    is_active = models.BooleanField(default=True,  verbose_name='Active Status')
    date_created =  models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    title = models.CharField(max_length=255, verbose_name =  'Title')

    class Meta:
        verbose_name =  'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']
    
    def __str__(self) -> str:
        return self.title

class Answer(UpdateModel):
    
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['id']
    
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    ans_text = models.CharField(max_length= 255, verbose_name = "Answer Text:-")
    is_right = models.BooleanField(default= False)

    def __str__(self) -> str:
        return super().ans_text
