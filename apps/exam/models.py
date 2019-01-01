from django.db import models
from apps.timetable.models import Table

class Exam(models.Model):
    '''考试表数据库模型'''

    examName = models.ForeignKey(Table, verbose_name='考试科目名', on_delete=models.CASCADE)

    time = models.DateTimeField(verbose_name='考试时间', blank=False, default='')
