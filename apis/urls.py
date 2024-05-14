from django.urls import path
from .views import StudentAverageGradesView, GroupAverageGradesView

urlpatterns = [
    path('api/student-average-grades/', StudentAverageGradesView.as_view()),
    path('api/group-average-grades/', GroupAverageGradesView.as_view()),
]
