# Generated by Django 3.1.5 on 2023-03-13 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_auto_20230313_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrollmanagement',
            name='payroll_installments',
        ),
        migrations.AddField(
            model_name='payrollinstallments',
            name='payroll_management',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payroll_installments', to='payroll.payrollmanagement'),
        ),
    ]
