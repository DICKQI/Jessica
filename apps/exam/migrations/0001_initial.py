# Generated by Django 2.0.4 on 2019-01-01 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timetable', '0007_auto_20190101_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default='', verbose_name='考试时间')),
                ('examName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Table', verbose_name='考试科目名')),
            ],
        ),
    ]