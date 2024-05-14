from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.auth_mixins import TeacherRequiredMixin, StudentRequiredMixin,AdminRequiredMixin
from .models import Teacher,Student


class HomePageForAdmin(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'school/home.html')


class TeacherSubjectPageView(TeacherRequiredMixin, View):
    def get(self,request):
        teacher = Teacher.objects.get(name=request.user.username)
        subjects = teacher.subjects.all()
        return render(request, 'school/subjects.html', {"subjects": subjects})


class StudentGradePageView(StudentRequiredMixin, View):
    def get(self,request):
        student = Student.objects.get(name=request.user.username)
        average_score= student.average_score()
        grades = student.grades.all()
        return render(request, 'school/grades.html', {"grades": grades, "average_score":average_score})
