from django.urls import path
from feedback.views import CreateFeedbackView, SuccessFeedbackView

urlpatterns = [
    path('create/', CreateFeedbackView.as_view(), name="create_feedback"),
    path('success/', SuccessFeedbackView.as_view(), name="success_feedback"),
]
