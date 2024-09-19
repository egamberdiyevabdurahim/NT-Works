from django.db import models
from django.contrib.auth.models import AbstractUser

from groups.models import GradeModel, GroupModel, CreatedAtsModel


class UsersModel(AbstractUser, CreatedAtsModel):
    STATUS = (
        ("Dekan", "Dekan"),
        ("Student", "Student"),
        ("Tyutor", "Tyutor"),
        ("Teacher", "Teacher"),
        ("Admin", "Admin")
    )
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField(null=True)
    role = models.CharField(choices=STATUS, max_length=15, default="Student")
    photo = models.ImageField(upload_to="users/photos/")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class StudentModel(models.Model):
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeModel, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.user}/{self.grade}/{self.group}"
