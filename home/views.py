from django.shortcuts import render
from django.views import View
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        today = datetime.today()
        user = request.user
        tasks = Task.objects.filter(is_active=True, user=user, date__gte=today)
        return render(request, 'home/home.html', {'tasks': tasks, 'user': user})
