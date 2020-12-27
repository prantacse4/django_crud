from django import forms
from first_app import models

class StudentForm(forms.ModelForm):
    
    class Meta:
        model =  models.StudentModel
        fields = "__all__"