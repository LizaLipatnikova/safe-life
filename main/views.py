from django.views.generic import ListView
from main.models import Post

# Класс-примесь, для указания дополнительной логики некоторым представлениям
# Данный класс добавляет в контекст шаблона индентификатор, который сообщаем меню сайта, какая страница активна
class MenuMixin:
    id_page = ""

    # Переопределяем метод, которые будет в других классах, добавляя дополнительную переменную
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_active_page"] = self.id_page
        return context
    

# Главная страница
class IndexView(MenuMixin, ListView):
    id_page = "index"
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
