from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.name


class ImageTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='image_task')
    image = models.ImageField()

    def __str__(self):
        return self.task.name
