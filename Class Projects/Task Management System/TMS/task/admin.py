from django.contrib import admin
from .models import TasksModel

# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display=['task_name','task_descp','task_added_at','task_status']



admin.site.register(TasksModel,AdminTask)