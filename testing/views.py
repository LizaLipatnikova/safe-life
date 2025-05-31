from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.mixins import MenuMixin

class StartTestingView(LoginRequiredMixin, MenuMixin, TemplateView):
    id_page = "test"
    template_name = "start_testing.html"
