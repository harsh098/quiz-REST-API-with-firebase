from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Category)
class CategoryAdminPanel(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(Quiz)
class QuizPanel(admin.ModelAdmin):
    
    list_display = [
        'id',
        'title',
        'is_active',
    ]

class AnswerSettings(admin.TabularInline):
    model = Answer
    fields = [
        'ans_text',
        'is_right',
    ]

@admin.register(Question)
class QuestionPanel(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'difficulty_level',
        
    ]
    list_display = [
        'title',
        'quiz',
        'date_updated',
        'difficulty_level',

    ]
    inlines = [
        AnswerSettings,
    ]

@admin.register(Answer)
class AnswerPanel(admin.ModelAdmin):

    list_display = [
        'ans_text',
        'is_right',
        'question',
    ]