from django.db import models
from django.contrib.auth.models import User

# Модель отзыва
class Feedback(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Отзыв",
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )
    text = models.TextField("Содержание")
    created_at = models.DateField("Дата написания", auto_now_add=True)

    def __str__(self):
        return f"Отзыв {self.user.username} от {self.created_at}"

    class Meta:
        # Сортируем по самым свежим отзывам
        ordering = ('-created_at',)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
