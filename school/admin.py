from django.contrib import admin
from .models import Student, Teacher, Subject, Grade, Group


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Group)
