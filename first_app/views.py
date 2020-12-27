from django.shortcuts import render
from first_app.models import StudentModel

# Create your views here.

def home(request):
    student_list = StudentModel.objects.order_by("name")
    diction={'title':"Home", 'student_list':student_list}
    return render(request, 'first_app/index.html', context = diction)


def student_info(request):
    diction={}
    return render(request, 'first_app/student_info.html', context = diction)


def student_form(request):
    diction={}
    return render(request, 'first_app/student_form.html', context = diction)


def update_info(request):
    diction={}
    return render(request, 'first_app/update_info.html', context = diction)