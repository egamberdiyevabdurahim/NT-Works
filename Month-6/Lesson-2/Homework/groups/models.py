from django.db import models
from django.conf import settings

class CreatedAtsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.created_at}/{self.updated_at}"

class GradeModel(models.Model):
    grade_level = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return str(self.grade_level)

class GroupModel(CreatedAtsModel, models.Model):
    name = models.CharField(max_length=50)
    tyutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    grade = models.ForeignKey(GradeModel, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name

class SubjectModel(models.Model):
    name = models.CharField(max_length=50)
    grade = models.ForeignKey(GradeModel, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name

class DailySubjectsModel(models.Model):
    name = models.CharField(max_length=64)
    group = models.ForeignKey(GroupModel, on_delete=models.SET_NULL, null=True)
    first = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='first')
    second = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='second')
    third = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='third')

    class Meta:
        verbose_name = "Daily Subject"
        verbose_name_plural = "Daily Subjects"

    def __str__(self):
        return self.name
