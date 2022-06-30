# Generated by Django 3.1.7 on 2022-06-26 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0022_auto_20220625_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField()),
                ('student_read', models.BooleanField(default=False)),
                ('supervisor_read', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.student')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.supervisor')),
            ],
        ),
    ]
