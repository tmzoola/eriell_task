from django.db import models
from django.contrib.auth.models import AbstractUser

STUDENT, TEACHER, ADMIN = ('student', 'teacher', 'admin')


class User(AbstractUser):
    USER_ROLES = (
        (STUDENT, STUDENT),
        (TEACHER,TEACHER),
        (ADMIN, ADMIN)
    )
    user_role = models.CharField(max_length=50, choices=USER_ROLES, default=STUDENT)

