from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):

    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'you registered', 'success')
            return redirect('accounts:user_login_view')
        return render('accounts:user_register_view')


class UserLoginView(View):

    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'your login', 'success')
            return redirect('home:home_view')
        return redirect('accounts:user_login_view')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'your logout', 'success')
        return redirect('accounts:user_login_view')