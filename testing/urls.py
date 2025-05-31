from django.urls import path
from testing.views import StartTestingView, QuestionsListView

urlpatterns = [
    path('start/', StartTestingView.as_view(), name="start_test"),
    path('', QuestionsListView.as_view(), name="testing"),
]