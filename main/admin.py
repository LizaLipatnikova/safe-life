from django.contrib import admin
from main.models import Post

# Регистрируем модель на административной панели с помощью декоратора
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Какие поля отображать в списке всех объектов модели
    list_display = ["title", "created_at",]
