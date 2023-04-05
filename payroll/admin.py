from django.contrib import admin
from .models import (
    PayrollManagement,
    PayrollInstallments,
)

admin.site.register(PayrollManagement)
admin.site.register(PayrollInstallments)
