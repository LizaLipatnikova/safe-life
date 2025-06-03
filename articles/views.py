from django.views.generic import ListView, DetailView
from articles.models import Article, Topic
from collections import defaultdict
from main.mixins import MenuMixin

# Список тем и статьей к ним
class TopicsView(MenuMixin, ListView):
    id_page = "articles"
    model = Topic
    template_name = "list_articles.html"
    context_object_name = "topics"

    # Получаем статьи и группируем их по темам
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()
        
        # Создаем defaultdict - вариацию словаря, которые при обращении к несуществующему ключу возращает значение по умолчанию
        grouped_articles = defaultdict(list)

        for article in articles:
            if article.topic:
                grouped_articles[article.topic].append(article)
            else:
                # Статьи без темы добавляем в отдельную группу
                grouped_articles[None].append(article)
        
        context["grouped_articles"] = grouped_articles
        return context

# Страница статьи
class ArticleView(MenuMixin, DetailView):
    id_page = "articles"
    model = Article
    template_name = "article.html"
    context_object_name = "article"
