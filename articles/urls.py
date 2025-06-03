from django.urls import path
from articles.views import TopicsView, ArticleView, export_docx

urlpatterns = [
    path('', TopicsView.as_view(), name="list_articles"),
    path('<int:pk>/', ArticleView.as_view(), name="article"),
    path('export/<int:pk>/', export_docx, name="export_article"),
]
