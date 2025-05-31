from django.urls import path
from testing.views import StartTestingView

urlpatterns = [
    path('', StartTestingView.as_view(), name="start_test"),
]