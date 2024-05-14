from django.urls import path
from .views import TeacherSubjectPageView, StudentGradePageView, HomePageForAdmin


app_name = 'school'

urlpatterns = [
    path('', HomePageForAdmin.as_view(), name="home"),
    path('subjects/', TeacherSubjectPageView.as_view(), name="teacher_subjects"),
    path('grades/', StudentGradePageView.as_view(), name="student_grades"),
]