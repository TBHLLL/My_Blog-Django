from django.contrib import admin
from .models import ArticlePost,ArticleColumn
from django.apps import AppConfig
from django.db import models

# admin.site.site_header = 'Blog�����̨'  # ����header
# admin.site.site_title = 'Blog�����̨'  # ����title
# admin.site.index_title = 'Blog�����̨'
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)



# class TasksConfig(AppConfig):
#     name = 'tasks'
#
#     verbose_name = '�������'
#
#
#
#
#
# class Status(models.TextChoices):
#     UNSTARTED = 'u', "Not started yet"
#     ONGOING = 'o', "Ongoing"
#     FINISHED = 'f', "Finished"
#
#
# class Task(models.Model):
#     name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
#     status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
#
#     class Meta:
#         verbose_name = "����"
#         verbose_name_plural = "����"
#
#     def __str__(self):
#         return self.name
# Register your models here.
