from django.views.generic import TemplateView

# Страница, сообщающая пользователя о необходимости атуентификации
class AuthWarningView(TemplateView):
    template_name = "auth_warning.html"
