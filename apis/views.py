from django.db.models import Avg
from django.db import connection
from rest_framework import generics
from rest_framework.response import Response
from school.models import Student, Grade
from users.permissions import IsStudent, IsTeacher
from rest_framework.permissions import IsAuthenticated


class StudentAverageGradesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request, *args, **kwargs):
        students = Student.objects.all().order_by('groups__name', 'name')
        response_data = []

        for student in students:
            student_avg_grades = Grade.objects.filter(student=student).values('subject__name').annotate(avg_grade=Avg('grade'))
            for entry in student_avg_grades:
                response_data.append({
                    'student_name': student.name,
                    'group': student.groups.first().name if student.groups.exists() else None,
                    'subject': entry['subject__name'],
                    'average_grade': entry['avg_grade']
                })

        return Response(response_data)


class GroupAverageGradesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT g.name AS group_name, s.name AS subject_name, AVG(gr.grade) AS average_grade
                FROM myapp_group g
                JOIN myapp_group_students gs ON gs.group_id = g.id
                JOIN myapp_student st ON st.id = gs.student_id
                JOIN myapp_grade gr ON gr.student_id = st.id
                JOIN myapp_subject s ON s.id = gr.subject_id
                GROUP BY g.name, s.name
            """)
            results = cursor.fetchall()

        response_data = [
            {
                'group': row[0],
                'subject': row[1],
                'average_grade': row[2]
            }
            for row in results
        ]

        return Response(response_data)
