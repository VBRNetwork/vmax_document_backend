# Generated by Django 3.1.5 on 2022-08-08 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0009_auto_20220729_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payroll_name', models.CharField(blank=True, max_length=255, null=True)),
                ('payroll_description', models.TextField(blank=True, null=True)),
                ('payroll_file', models.FileField(blank=True, null=True, upload_to='payroll/')),
                ('payroll_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name': 'Payroll Management',
                'verbose_name_plural': 'Payroll Management',
            },
        ),
        migrations.AddIndex(
            model_name='payrollmanagement',
            index=models.Index(fields=['payroll_name'], name='payroll_pay_payroll_64fdaf_idx'),
        ),
        migrations.AddIndex(
            model_name='payrollmanagement',
            index=models.Index(fields=['id'], name='payroll_pay_id_d81fa6_idx'),
        ),
    ]
