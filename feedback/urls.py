from django.urls import path
from feedback.views import CreateFeedbackView

urlpatterns = [
    path('create/', CreateFeedbackView.as_view(), name="create_feedback"),
]
