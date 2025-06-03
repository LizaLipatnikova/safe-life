from django.urls import path
from feedback.views import CreateFeedbackView, SuccessFeedbackView, ListFeedbacksView

urlpatterns = [
    path('create/', CreateFeedbackView.as_view(), name="create_feedback"),
    path('success/', SuccessFeedbackView.as_view(), name="success_feedback"),
    path('list/', ListFeedbacksView.as_view(), name="list_feedbacks"),
]
