# Generated by Django 4.0.6 on 2022-07-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]