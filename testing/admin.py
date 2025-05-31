from django.contrib import admin
from testing.models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "weight", ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question__question", "answer", "is_correct",]

    def question__question(self, obj):
        return obj.question.question

    question__question.short_description = "Вопрос"
