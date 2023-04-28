from django.contrib import admin
from .models import LeaveType, EmployeesLeaves

admin.site.register(LeaveType)
admin.site.register(EmployeesLeaves)