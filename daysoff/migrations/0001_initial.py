# Generated by Django 3.1.5 on 2023-04-19 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Leave Type',
                'verbose_name_plural': 'Leave Types',
            },
        ),
        migrations.CreateModel(
            name='EmployeesLeaves',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_leaves', to=settings.AUTH_USER_MODEL)),
                ('leave_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_leaves', to='daysoff.leavetype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_leaves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Leave',
                'verbose_name_plural': 'Employee Leaves',
                'ordering': ['-id'],
            },
        ),
    ]