# Generated by Django 3.1.7 on 2022-06-25 02:29

from django.db import migrations, models
import studentSupervisor.models


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0019_auto_20220625_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuplaod',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=studentSupervisor.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='projectuplaod',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to=studentSupervisor.models.user_directory_path),
        ),
    ]