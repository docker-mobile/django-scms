# Generated by Django 3.1.8 on 2021-06-17 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0007_auto_20210503_0654'),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='_class',
        ),
        migrations.AddField(
            model_name='topic',
            name='_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sis.classlevel'),
        ),
    ]
