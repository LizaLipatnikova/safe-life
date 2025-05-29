from django.urls import path
from articles.views import TopicsView

urlpatterns = [
    path('', TopicsView.as_view(), name="articles")
]
