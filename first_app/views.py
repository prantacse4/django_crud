from django.shortcuts import render
from first_app.models import StudentModel
from first_app import forms

# Create your views here.

def home(request):
    student_list = StudentModel.objects.order_by("name")
    diction={'title':"Home", 'student_list':student_list}
    return render(request, 'first_app/index.html', context = diction)


def student_form(request):
    new_form = forms.StudentForm()

    if  request.method == "POST":
        new_form = forms.StudentForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)

    diction={'title':"StudentForm", "student_form":new_form}
    return render(request, 'first_app/student_form.html', context = diction)



def student_info(request, student_id):
    student_info = StudentModel.objects.get(pk=student_id)
    diction={'student_info':student_info}
    return render(request, 'first_app/student_info.html', context = diction)



def update_info(request, student_id):
    student_info = StudentModel.objects.get(pk = student_id)
    form = forms.StudentForm(instance = student_info)

    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
    diction={'student_form':form}
    return render(request, 'first_app/update_info.html', context = diction)


def delete_info(request, student_id):
    delete_info = StudentModel.objects.get(pk=student_id).delete()
    mgs = "Deleted Successfully"
    diction = {'mgs':mgs}
    return render(request, 'first_app/index.html', context = diction)

