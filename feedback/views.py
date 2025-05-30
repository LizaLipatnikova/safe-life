from django.forms import BaseModelForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from main.mixins import MenuMixin

# Страница создания отзыва
class CreateFeedbackView(LoginRequiredMixin, MenuMixin, CreateView):
    id_page = "feedback"
    model = Feedback
    template_name = "create_feedback.html"
    
    # Класс формы, которая будет ренедерить html код формы
    form_class = FeedbackForm

    # Маршрут при успешном создании отзыва
    # reverse_lazy необходима, чтобы получить маршрут по имени в момент работы этого запроса
    # Иначе django применит маршрут во время запуска сервера и может не найти маршруты, поскольку еще не успел их загрузить
    success_url = reverse_lazy("success_feedback")

    # Переопределяем метод проверки формы. Добавляем текущего пользователя к объекту отзыва, чтобы установить авторство
    def form_valid(self, form: BaseModelForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
