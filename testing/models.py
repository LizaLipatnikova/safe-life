from django.db import models

class Question(models.Model):
    question = models.CharField("Вопрос", max_length=200)
    weight = models.IntegerField("Вес вопроса", default=2)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос", related_name="answers")
    answer = models.CharField("Ответ", max_length=150)
    is_correct = models.BooleanField("Правильный ответ", default=False)

    def __str__(self):
        return f"{self.question.question}: {self.answer}"
    
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
