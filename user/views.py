from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from main.mixins import MenuMixin
from user.forms import UpdateUserForm

# Страница, сообщающая пользователя о необходимости атуентификации
class AuthWarningView(TemplateView):
    template_name = "auth_warning.html"

# Авторизация
class UserLoginView(LoginView):
    template_name = "login.html"

# Регистрация
class RegistrationView(CreateView):
    model = User
    template_name = "registration.html"
    success_url = reverse_lazy("login")
    form_class = UserCreationForm

# Личный кабинет
class AccountView(LoginRequiredMixin, MenuMixin, TemplateView):
    id_page = "account"
    template_name = "account.html"

# Редактирование аккаунта пользователя
class AccountEditView(LoginRequiredMixin, MenuMixin, UpdateView):
    id_page = "account"
    template_name = "account_edit.html"
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy("account")

# Выход из аккаунта. LogoutView не имеет специфических настроек, поэтому класс пустой
class UserLogoutView(LogoutView):
    pass
