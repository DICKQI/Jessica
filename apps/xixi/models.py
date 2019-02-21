from django.db import models

# Create your models here.
class xxTable(models.Model):
    '''课表数据库模型'''

    Single_or_double_choice = {
        ('单周', '单周'),
        ('双周', '双周'),
        ('单双周', '单双周')
    }

    classname = models.CharField(verbose_name='课程名称', default='', max_length=100)

    single_or_double = models.CharField(verbose_name='单双周', default='s', choices=Single_or_double_choice, max_length=3)

    beginWeek = models.CharField(verbose_name='起始周', default='', max_length=100)

    endWeek = models.CharField(verbose_name='结束周', default='', max_length=100)

    week = models.CharField(verbose_name='周几开课', default='', max_length=100)

    beginTime = models.CharField(verbose_name='开始节数', default='1', max_length=2)

    endTime = models.CharField(verbose_name='结束节数', default='2', max_length=2)

    classroom = models.CharField(verbose_name='教室', default='', max_length=100)

    teacher = models.CharField(verbose_name='老师名称', default='', max_length=100)

    egg = models.CharField(verbose_name='彩蛋', default='', max_length=100, blank=True)

    def __str__(self):
        return self.classname

    class Meta:
        verbose_name = '课表'
        verbose_name_plural = verbose_name + '列表'
        ordering = ['beginTime']
        db_table = 'xxtimetable'