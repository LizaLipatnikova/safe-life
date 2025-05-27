from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit

# Модель новостей на главной странице
class Post(models.Model):
    title = models.CharField("Заголовок", max_length=120)
    desc = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="image_posts/") 

    # Преобразуем изображение к нужному размеру и формату
    # Данное поле не будет в базе данных, оно просто автоматические создаст в папке медиа-файлов нужное изображение
    format_image = ImageSpecField([ResizeToFit(width=500), ], source="image", format="PNG")

    # Дата создания. Поле заполняется автоматически
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # Сортируем по самым свежим новостям
        ordering = ('-created_at',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
