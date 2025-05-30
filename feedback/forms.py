from django import forms
from feedback.models import Feedback

# Форма для отзыва
class FeedbackForm(forms.ModelForm):
    # Настройки для формы на основе модели
    class Meta:
        model = Feedback # Какую модель использовать
        fields = ["text", ] # Какие поля показать в форме

    # Переопределяем конструктор, чтобы поменять метку поля на более понятную, поскольку мы в форме используем лишь одно поле
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = 'Отзыв'
