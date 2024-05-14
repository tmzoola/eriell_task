from django.urls import path
from .views import LoginPageView, RegisterPageView

app_name = 'users'

urlpatterns = [
    path('login-page/',LoginPageView.as_view(), name='login_page'),
    path('register-page/',RegisterPageView.as_view(), name='register'),

]