from django.http import HttpResponse
from django.shortcuts import render
from .models import aoexam

def exam_list(request):
    exams = aoexam.objects.all()  # Получаем все экзамены
    return render(request, 'exam.html', {'exams': exams})

def home(request):
    return HttpResponse("Welcome to the Warehouse Management System!")


def exam_list(request):
    exams = aoexam.objects.all()
    context = {
        'exams': exams,
        'title': 'Список экзаменов',
        'student_name': 'Ваше ФИО',
        'group_number': 'Ваш номер группы'
    }
    return render(request, 'exam_list.html', context)