"""
URL configuration for safeLife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include("feedback.urls")),
    path('articles/', include("articles.urls")),
    path('test/', include("testing.urls")),
    path('user/', include("user.urls")),
    path('', include("main.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')), # Пути для редактора
]

# Добавляем обработку медиа-файлов в режиме разработки
# При развертывании в производственной среде, за обработку медиа-файлов будет отвечать производственный сервер
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
