from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.mixins import MenuMixin
from testing.models import Question
import random

class StartTestingView(LoginRequiredMixin, MenuMixin, TemplateView):
    id_page = "test"
    template_name = "start_testing.html"

class QuestionsListView(LoginRequiredMixin, MenuMixin, ListView):
    id_page = "test"
    model = Question
    template_name = "testing.html"
    context_object_name = "questions"

    # Случайным образом мешаем вопросы
    def get_queryset(self):
        questions = Question.objects.all()
        random.shuffle(list(questions))
        return questions
