# Класс-примесь, для указания дополнительной логики некоторым представлениям
# Данный класс добавляет в контекст шаблона индентификатор, который сообщаем меню сайта, какая страница активна
class MenuMixin:
    id_page = ""

    # Переопределяем метод, которые будет в других классах, добавляя дополнительную переменную
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_active_page"] = self.id_page
        return context
