
from django.contrib import admin
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('student_form/',views.student_form, name="student_form"),
    path('student_info/',views.student_info, name="student_info"),
    path('update_info/',views.update_info, name="update_info"),

]
