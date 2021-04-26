# Generated by Django 3.1.2 on 2021-04-26 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0004_auto_20210426_1130'),
        ('sis', '0003_auto_20210424_2015'),
        ('users', '0002_auto_20210424_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='"Present" will not be saved but may show as a teacher option.', max_length=255, unique=True)),
                ('code', models.CharField(help_text='Short code used on attendance reports. Ex: A might be the code for the name Absent', max_length=10, unique=True)),
                ('excused', models.BooleanField(default=False)),
                ('absent', models.BooleanField(default=False, help_text='Some statistics need to add various types of absent statuses, such as the number in parentheses in daily attendance.')),
                ('tardy', models.BooleanField(default=False, help_text='Some statistics need to add various types of tardy statuses, such as the number in parentheses in daily attendance.')),
                ('half', models.BooleanField(default=False, help_text='Half attendance when counting. DO NOT check off absent otherwise it will double count!')),
            ],
            options={
                'verbose_name_plural': 'Attendance Statuses',
            },
        ),
        migrations.CreateModel(
            name='TeachersAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_in', models.TimeField(blank=True)),
                ('time_out', models.TimeField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.attendancestatus')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
            options={
                'ordering': ('-date', 'teacher'),
                'unique_together': {('teacher', 'date', 'status')},
            },
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('ClassSection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.classsection')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.attendancestatus')),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sis.student')),
            ],
            options={
                'ordering': ('-date', 'student'),
                'unique_together': {('student', 'date', 'status')},
            },
        ),
    ]
