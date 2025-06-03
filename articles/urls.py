from django.urls import path
from articles.views import TopicsView, ArticleView

urlpatterns = [
    path('', TopicsView.as_view(), name="list_articles"),
    path('<int:pk>/', ArticleView.as_view(), name="article")
]
