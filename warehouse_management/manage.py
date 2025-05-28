#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
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


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse_management.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
