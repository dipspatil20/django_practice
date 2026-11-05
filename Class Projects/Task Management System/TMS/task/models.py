from django.db import models

# Create your models here.
class TasksModel(models.Model):
    task_name=models.CharField(max_length=30)
    task_descp=models.CharField(max_length=50)
    task_added_at=models.DateTimeField(auto_now_add=True)
    task_status=models.BooleanField(default=True)


class CategoryModel(models.Model):
    cat = models.CharField(max_length=30)
    def __str__(self):
        return self.cat

class UserTaskModel(models.Model):
    cat = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    task = models.ForeignKey(TasksModel, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)