from django.shortcuts import render,redirect
from django.views import View
from .forms import AddTaskForm, AddImageToTaskForm
from .models import Task, ImageTask
from django.contrib import messages
from datetime import datetime


class AddTask(View):
    form_class = AddTaskForm
    form_image_class = AddImageToTaskForm

    def get(self, request):
        form = self.form_class()
        image_form = self.form_image_class()
        return render(request, 'todo/add_task.html', {'form': form, 'image_form': image_form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        image_form = self.form_image_class(request.POST, request.FILES)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()

            if image_form.is_valid():
                for img in request.FILES.getlist('image'):
                    ImageTask.objects.create(task=new_task, image=img)
                messages.success(request, 'good', 'success')
            return redirect('home:home_view')
        return redirect('todo:add_task')


class DoneTask(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.is_active = False
        task.save()
        messages.success(request, 'the task was done', 'success')
        return redirect('home:home_view')
    

class DetailTask(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        images = ImageTask.objects.filter(task=task)
        return render(request, 'todo/detail.html', {'task': task, 'images': images})


class OldTask(View):
    def get(self, request):
        title_search_query = request.GET.get('Title_search')
        Description_search_query = request.GET.get('Description_search')
        sdate_search_query = request.GET.get('sdate_search')
        edate_search_query = request.GET.get('edate_search')
        status_search = request.GET.get('status_search')

        today = datetime.today()
        user = request.user
        tasks = Task.objects.filter(user=user, date__lt=today)
        checked = ''

        if title_search_query != '' and title_search_query is not None:
            tasks = tasks.filter(name__contains=title_search_query)
        if Description_search_query != '' and Description_search_query is not None:
            tasks = tasks.filter(description__contains=Description_search_query)
        if Description_search_query != '' and Description_search_query is not None:
            tasks = tasks.filter(description__contains=Description_search_query)
        if sdate_search_query != '' and sdate_search_query is not None:
            tasks = tasks.filter(date__gte=sdate_search_query)
        if edate_search_query != '' and edate_search_query is not None:
            tasks = tasks.filter(date__lte=edate_search_query)
        if status_search == 'yes':
            tasks = tasks.filter(is_active=False)
            checked = 'checked'

        return render(request, 'todo/old_task.html', {'tasks': tasks, 'checked': checked})
