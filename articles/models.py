from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Модель темы (главы)
class Topic(models.Model):
    title = models.CharField("Название темы", max_length=120)

    def __str__(self):
        return self.title
    
    class Meta:
        # Сортируем по алфавиту
        ordering = ('title',)
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

# Модель статьей
class Article(models.Model):
    title = models.CharField("Заголовок", max_length=140)
    
    # Настраиваем внешнюю связь "Один ко многим"
    topic = models.ForeignKey(
        Topic, # С какой моделью связываемся
        verbose_name="Тема", # Имя поля, которое будет отображаться у пользователя
        on_delete=models.SET_NULL, # Поведение при удалении, в нашем случае поле будет иметь значение null
        null=True, # Может ли поле в таблице быть пустым
        blank=True, # Может ли поле в формах быть необязательным
        related_name="articles", # Обратное имя, для обращения к статьями из модели темы
    )
    content = CKEditor5Field("Содержиоме статьи") # Поле "богатого" текста (с списками, таблицами, жирными текстом и т.д.)
    update_at = models.DateField("Дата обновления", auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        # Сортируем начиная с недавно обновленных статьей
        ordering = ("-update_at", )
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

