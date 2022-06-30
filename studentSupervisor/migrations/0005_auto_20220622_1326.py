# Generated by Django 3.1.7 on 2022-06-22 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0004_auto_20220622_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuplaod',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.student'),
        ),
        migrations.AlterField(
            model_name='projectuplaod',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('declined', 'declined')], default='pending', max_length=255, null=True),
        ),
    ]