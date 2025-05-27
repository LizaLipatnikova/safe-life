from django.contrib import admin
from articles.models import Article, Topic

admin.site.register(Topic)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Поля для отображения в списке модели на административной панели
    list_display = ["title", "topic__title", "update_at", ]

    # Поскольку поля "topic__title" несуществует в модели, то мы задаем его программно через функцию
    def topic__title(self, obj):
        return obj.topic.title
    
    topic__title.short_description = "Тема" # Подпись поля
