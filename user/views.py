from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Страница, сообщающая пользователя о необходимости атуентификации
class AuthWarningView(TemplateView):
    template_name = "auth_warning.html"

# Авторизация
class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("account")

# Регистрация
class RegistrationView(CreateView):
    model = User
    template_name = "registration.html"
    success_url = reverse_lazy("login")
    form_class = UserCreationForm

# Личный кабинет
class AccountView(TemplateView):
    template_name = "account.html"

# Выход из аккаунта. LogoutView не имеет специфических настроек, поэтому класс пустой
class UserLogoutView(LogoutView):
    pass
