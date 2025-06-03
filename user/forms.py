from django import forms
from django.contrib.auth.models import User
from user.models import Profile

# Форма обновления пользователя в личном кабинете
class UpdateUserForm(forms.ModelForm):
    # Поле из профиля
    avatar = forms.ImageField(label="Аватар", required=False)

    class Meta:
        model = User # На основе которой модели создаем
        fields = ["email",] # Поля, которые надо включить в форму (берет только из User)

    # При инцилизации формы достаем значения из профиля
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Если у объекта есть профиль
        if self.instance.profile:
            self.fields['avatar'].initial = self.instance.profile.avatar

    def save(self, commit=True):
        # commit отвечает за сохранение базе данных
        user = super().save(commit)
        profile = user.profile

        # Сохраняем аватар
        profile.avatar = self.cleaned_data['avatar']
        profile.save()

        return user
