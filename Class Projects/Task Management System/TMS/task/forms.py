from django import forms
from .models import TasksModel, CategoryModel, UserTaskModel


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TasksModel
        fields=['task_name','task_descp','task_status']

class UserTaskModelForm(forms.ModelForm):
    class Meta:
        model = UserTaskModel
        fields = ['cat','task','status']


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['cat']
