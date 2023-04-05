from django.db import models
from users.models import User
from datetime import datetime

class Departments(models.Model):
    
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255, blank=True, null=True)
    department_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.department_name
    
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
    
class Teams(models.Model):

    id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    team_description = models.TextField(blank=True, null=True)
    team_location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Team: {self.team_name} | Location: {self.team_location}"
    
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        get_latest_by = "created_at"

class TeamMembers(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='team_members')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    organizational_level = models.IntegerField(blank=True, null=True)
    member_start_date = models.DateField(blank=True, null=True)
    is_teamleader = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, blank=True, null=True, related_name='team_members')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, blank=True, null=True, related_name='team_members')

    @property
    def member_tenure(self):
        return datetime.date.today() - self.member_start_date

    def __str__(self):
        return f"User: {self.user.username} | Team: {self.team} | Department: {self.department}"

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
