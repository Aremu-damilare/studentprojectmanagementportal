# Generated by Django 3.1.7 on 2022-06-22 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0002_auto_20220622_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.supervisor'),
        ),
        migrations.AlterField(
            model_name='projectuplaod',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.project'),
        ),
    ]
