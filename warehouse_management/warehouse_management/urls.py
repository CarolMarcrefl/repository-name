from django.contrib import admin
from django.urls import path
from companies.views import home, exam_list  # Импортируем представление exam_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Этот маршрут обрабатывает корневой путь
    path('exams/', exam_list, name='exam_list_temp'),  # Этот маршрут для страницы с экзаменами
    path('exam/', exam_list, name='exam_list_temp_short'),  # Новый маршрут для exam/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
