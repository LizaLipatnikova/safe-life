from django.views.generic import ListView, TemplateView
from main.models import Post
from main.mixins import MenuMixin

# Главная страница
class IndexView(MenuMixin, ListView):
    id_page = "index"
    model = Post
    context_object_name = "posts"
    template_name = "index.html"

# Страница "О нас"
class AboutView(MenuMixin, TemplateView):
    id_page = "about"
    template_name = "about.html"
