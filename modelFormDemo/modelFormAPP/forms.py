from django import forms
from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'startProject' : forms.DateInput(format='%Y-%m-%d',attrs={"type":"date"},),
            'endProject': forms.DateInput(format='%Y-%m-%d',attrs={"type":"date"})
        }