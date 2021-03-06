# Generated by Django 2.1.2 on 2019-02-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kkTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(default='', max_length=100, verbose_name='课程名称')),
                ('single_or_double', models.CharField(choices=[('双周', '双周'), ('单双周', '单双周'), ('单周', '单周')], default='s', max_length=3, verbose_name='单双周')),
                ('beginWeek', models.CharField(default='', max_length=100, verbose_name='起始周')),
                ('endWeek', models.CharField(default='', max_length=100, verbose_name='结束周')),
                ('week', models.CharField(default='', max_length=100, verbose_name='周几开课')),
                ('beginTime', models.CharField(default='1', max_length=2, verbose_name='开始节数')),
                ('endTime', models.CharField(default='2', max_length=2, verbose_name='结束节数')),
                ('classroom', models.CharField(default='', max_length=100, verbose_name='教室')),
                ('teacher', models.CharField(default='', max_length=100, verbose_name='老师名称')),
                ('egg', models.CharField(blank=True, default='', max_length=100, verbose_name='彩蛋')),
            ],
            options={
                'verbose_name': '课表',
                'verbose_name_plural': '课表列表',
                'db_table': 'timetable',
                'ordering': ['beginTime'],
            },
        ),
    ]
