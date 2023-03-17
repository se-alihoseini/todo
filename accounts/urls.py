from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register_view'),
    path('login/', views.UserLoginView.as_view(), name='user_login_view'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout_view'),

]