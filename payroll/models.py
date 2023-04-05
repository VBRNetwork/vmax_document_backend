from django.db import models
from users.models import User

class PayrollInstallments(models.Model):

    id = models.AutoField(primary_key=True)
    payroll_installment_name = models.CharField(max_length=255, blank=True, null=True)
    payroll_installment_description = models.TextField(blank=True, null=True)
    payroll_installment_amount_gross = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_installment_amount_net = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_installment_amount_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_installment_amount_deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_installment_date = models.DateField(auto_now_add=True, blank=True, null=True)
    payroll_installment_file = models.FileField(upload_to='payroll/', blank=True, null=True)
    payroll_management = models.ForeignKey('PayrollManagement', on_delete=models.CASCADE, blank=True, null=True, related_name='payroll_installments')

    def __str__(self):
        return f"{self.payroll_installment_name} | {self.id}"
    
    class Meta:
        indexes = [
            models.Index(fields=["payroll_installment_name"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "Payroll Installment"
        verbose_name_plural = "Payroll Installments"

class PayrollManagement(models.Model):

    id = models.AutoField(primary_key=True)
    payroll_name = models.CharField(max_length=255, blank=True, null=True)
    payroll_description = models.TextField(blank=True, null=True)
    payroll_salary_gross = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_salary_net = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_salary_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_salary_deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payroll_date_added = models.DateField(auto_now_add=True, blank=True, null=True)
    payroll_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='payroll_user')

    def __str__(self):
        return f"{self.payroll_name} | {self.payroll_user.first_name}, {self.payroll_user.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=["payroll_name"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "Payroll Management"
        verbose_name_plural = "Payroll Management"


