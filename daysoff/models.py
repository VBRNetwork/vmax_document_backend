from django.db import models
from users.models import User

APPROVED_STATUS = (
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
    ("Pending", "Pending"),
)

class LeaveType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"

class EmployeesLeaves(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="employees_leaves")
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, blank=True, null=True, related_name="employees_leaves")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    approved_status = models.CharField(max_length=255, choices=APPROVED_STATUS, default="Pending")
    handled_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="approved_leaves")
    approved_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} | {self.leave_type.name} | {self.start_date} | {self.end_date}"
    
    class Meta:
        verbose_name = "Employee Leave"
        verbose_name_plural = "Employee Leaves"
        ordering = ["-id"]
