# Generated by Django 4.1 on 2023-09-17 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_topic_subject'),
        ('administration', '0014_academicyear_day_school_delete_classjournal'),
        ('schedule', '0017_alter_dailytimetable_id_alter_period_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='_class',
        ),
        migrations.RemoveField(
            model_name='period',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='period',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='weeklytimetable',
            name='wednesday',
        ),
        migrations.DeleteModel(
            name='DailyTimeTable',
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='WeeklyTimeTable',
        ),
    ]