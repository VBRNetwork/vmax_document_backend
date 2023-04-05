from documentmanager.celery import app
from .models import (
    PayrollManagement,
    PayrollInstallments
)

@app.task
def generate_monthly_payroll_installments():
    payroll = PayrollManagement.objects.all()
    for p in payroll:
        PayrollInstallments.objects.create(
            payroll=p,
            amount=p.amount,
            installment_date=p.installment_date,
            installment_number=1,
            status='pending'
        )