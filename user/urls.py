from django.urls import path
from user.views import AuthWarningView

urlpatterns = [
    path('warning/', AuthWarningView.as_view(), name="auth_warning"),
]
