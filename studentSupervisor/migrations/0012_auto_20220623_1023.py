# Generated by Django 3.1.7 on 2022-06-23 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0011_auto_20220622_1923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='ProjectComment',
        ),
        migrations.CreateModel(
            name='DefenceCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('approved', 'approved'), ('closed', 'closed')], default='pending', max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('mid_term', 'mid_term'), ('final', 'final')], default='final', max_length=255, null=True)),
                ('student_read', models.BooleanField(default=False)),
                ('supervisor_read', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.student')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentSupervisor.supervisor')),
            ],
        ),
    ]