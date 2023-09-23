# Generated by Django 4.1 on 2023-09-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_teacher_options_remove_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountant',
            options={'ordering': ('first_name', 'last_name')},
        ),
        migrations.RemoveField(
            model_name='accountant',
            name='user',
        ),
        migrations.AddField(
            model_name='accountant',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='accountant',
            name='alt_email',
            field=models.EmailField(blank=True, help_text='Personal Email apart from the one given by the school', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='accountant',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AddField(
            model_name='accountant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images'),
        ),
        migrations.AddField(
            model_name='accountant',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountant',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='accountant',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='accountant',
            name='national_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='accountant',
            name='username',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images'),
        ),
    ]
