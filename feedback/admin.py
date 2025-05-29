from django.contrib import admin
from feedback.models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["user__username", "created_at", ]

    # Программное поле user__username
    def user__username(self, obj):
        return obj.user.username
    
    user__username.short_description = "Пользователь" # Подпись поля
