from django.views.generic import ListView
from main.models import Post
from main.mixins import MenuMixin

# Главная страница
class IndexView(MenuMixin, ListView):
    id_page = "index"
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
