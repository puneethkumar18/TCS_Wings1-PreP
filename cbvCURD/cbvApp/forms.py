from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Mata:
        model = Student
        fields = '__all__'