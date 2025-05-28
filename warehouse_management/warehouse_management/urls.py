from django.contrib import admin
from django.urls import path
from companies.views import home, exam_list  # Импортируем представление exam_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Этот маршрут обрабатывает корневой путь
    path('exams/', exam_list, name='exam_list'),  # Новый маршрут для страницы с экзаменами
]
