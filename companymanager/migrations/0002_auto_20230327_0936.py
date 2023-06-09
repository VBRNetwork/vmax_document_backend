# Generated by Django 3.1.5 on 2023-03-27 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companymanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='departments',
            name='department_logo',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='department_manager',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='department_participants',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='department_teams',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='team_leader',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='team_manager',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='team_members',
        ),
        migrations.AddField(
            model_name='teams',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member_start_date', models.DateField(blank=True, null=True)),
                ('is_teamleader', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='companymanager.departments')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='companymanager.teams')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
