from django.contrib import admin
from django.contrib.auth.models import User
from .models import aoexam


class ExamAdmin(admin.ModelAdmin):
    # Поля, которые отображаются в списке
    list_display = ('exam_name', 'created_at', 'exam_date', 'is_public')

    # Поиск по названию экзамена и email пользователя
    search_fields = ('exam_name', 'users__email')  # users__email - связь с User

    # Фильтр по is_public и дате создания
    list_filter = ('is_public', 'created_at')

    # Иерархия по дате экзамена (появится под строкой поиска)
    date_hierarchy = 'exam_date'

    # Удобное редактирование M2M (users) - два списка
    filter_horizontal = ('users',)

    # Чтобы избежать проблем с загрузкой изображений в админке
    readonly_fields = ('exam_image_preview',)

    def exam_image_preview(self, obj):
        if obj.exam_image:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="150" />', obj.exam_image.url)
        return "Нет изображения"

    exam_image_preview.short_description = "Превью изображения"


# Регистрация модели в админке
admin.site.register(aoexam, ExamAdmin)