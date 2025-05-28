from django.views.generic import ListView
from main.models import Post

# Главная страница
class IndexView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index.html"
