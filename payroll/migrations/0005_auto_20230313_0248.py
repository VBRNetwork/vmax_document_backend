# Generated by Django 3.1.5 on 2023-03-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_remove_payrollmanagement_payroll_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrollmanagement',
            name='payroll_salary_deductions',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payrollmanagement',
            name='payroll_salary_gross',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payrollmanagement',
            name='payroll_salary_net',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payrollmanagement',
            name='payroll_salary_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
