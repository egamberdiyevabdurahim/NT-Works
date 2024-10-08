# Generated by Django 5.1.1 on 2024-09-19 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='DailySubjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.grademodel')),
            ],
            options={
                'verbose_name': 'Daily Subject',
                'verbose_name_plural': 'Daily Subjects',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.grademodel')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
    ]
