# Generated by Django 3.1.7 on 2022-06-25 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentSupervisor', '0017_auto_20220623_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('done', 'done'), ('closed', 'closed')], default='active', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='MeetingComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('verified_by_supervisor', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='studentSupervisor.meeting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_meeting_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]