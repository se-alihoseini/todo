from django.contrib import admin
from .models import Task,ImageTask


class ImageTaskAdmin(admin.TabularInline):
    model = ImageTask


@admin.register(Task)
class TaskRegister(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_active')
    inlines = (ImageTaskAdmin,)

