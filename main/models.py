from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit
from solo.models import SingletonModel
from django_ckeditor_5.fields import CKEditor5Field

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

# Создаем отдельную модель для редактирования содержимого на главной странице
# Поскольку любую информацию Django хранит в виде таблиц, мы используем специальную модель
# SingletonModel - это таблица только с одной записью, которая нужна для глобального содержимого сайта
class IndexContent(SingletonModel):
    text = models.TextField(
        "Текст",
        default="Приветствуем вас на сайте!",
        help_text="Данный текст будет отображаться на главной странице в верхней части"
    )
    
    def __str__(self):
        return "Приветствие главной страницы"

    class Meta:
        verbose_name = "Приветствие главной страницы"

class About(SingletonModel):
    text = CKEditor5Field("Текст страницы", default="О нас")

    def __str__(self):
        return "Страница 'О нас'"
    
    class Meta:
        verbose_name = "Страница 'О нас'"
