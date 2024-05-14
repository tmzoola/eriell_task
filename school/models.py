from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def average_score(self):
        avg_score = Grade.objects.filter(student=self).aggregate(Avg('grade'))['grade__avg']
        return avg_score if avg_score is not None else 0


class Group(models.Model):
    name = models.CharField(max_length=40, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups')
    student = models.ManyToManyField(Student, related_name='groups')


class Subject(models.Model):
    name = models.CharField(max_length=100)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='grades')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None and Grade.objects.filter(subject=self.subject, student=self.student).exists():
            raise ValidationError("This student already too his score from this subject")
        super(Grade, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.student}'s grade in {self.subject}: {self.grade}"

