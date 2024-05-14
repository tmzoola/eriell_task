from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from .models import TEACHER,STUDENT
from school.models import Teacher,Student
from .auth_mixins import AdminRequiredMixin


class LoginPageView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'users/login.html', context={"form": form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.user_role == TEACHER:
                    return redirect('school:teacher_subjects')
                elif user.user_role == STUDENT:
                    return redirect('school:student_grades')


class RegisterPageView(AdminRequiredMixin,View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', context={"form": form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            data = form.cleaned_data
            if data['user_role'] == TEACHER:
                teacher = Teacher()
                teacher.name = data['username']
                teacher.email = data['email']
                teacher.save()
                form.save()
                return redirect('/')
            elif data['user_role'] == STUDENT:
                student = Student()
                student.name = data['username']
                student.save()
                form.save()
                return redirect('/')

        return render(request, 'users/register.html', context={"form": form})
