from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class oaexam(models.Model):
    exam_name = models.CharField(max_length=255, verbose_name="Название экзамена")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания записи")
    exam_date = models.DateTimeField(verbose_name="Дата проведения экзамена")
    exam_image = models.ImageField(upload_to='exam_images/', verbose_name="Изображение задания")
    users = models.ManyToManyField(User, verbose_name="Пользователи, которые должны писать экзамен")
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"
