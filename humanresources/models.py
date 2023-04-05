from django.db import models

# HR_FILE_TYPES = (
#     ('Adv', 'Adv'),
#     ('Medical', 'Medical Leave'),
#     ('Warning', 'Warning'),
# )

RECRUITMENT_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)
class HrFileRequest(models.Model):

    id = models.AutoField(primary_key=True)
    hr_file_request_name = models.CharField(max_length=255, blank=True, null=True)
    hr_file_request_date_created = models.CharField(max_length=255, blank=True, null=True)
    hr_request_user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    hr_file_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.hr_file_request_name} | {self.hr_file_request_date_created}"

    class Meta:
        indexes = [
            models.Index(fields=["hr_file_request_name"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "HR File Request"
        verbose_name_plural = "HR File Request"

class HrFiles(models.Model):

    id = models.AutoField(primary_key=True)
    hr_file_name = models.CharField(max_length=255, blank=True, null=True)
    hr_file_date_created = models.CharField(max_length=255, blank=True, null=True)
    hr_adv_file = models.FileField(upload_to='hr/adv/', blank=True, null=True)
    hr_adv_user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    hr_medical_leave_file = models.FileField(upload_to='hr/medical/', blank=True, null=True)
    hr_warning_file = models.FileField(upload_to='hr/warning/', blank=True, null=True)
    hr_file_request = models.ForeignKey(HrFileRequest, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.hr_file_name} | {self.hr_adv_user.first_name}, {self.hr_adv_user.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=["hr_file_name"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "HR Files"
        verbose_name_plural = "HR Files"


class RecruitmentLeads(models.Model):

    id = models.AutoField(primary_key=True)
    recruitment_name = models.CharField(max_length=255, blank=True, null=True)
    recruitment_status = models.CharField(max_length=255, choices=RECRUITMENT_STATUS, default='Pending')
    recruitment_job_title = models.CharField(max_length=255, blank=True, null=True)
    recruitment_job_description = models.TextField(blank=True, null=True)
    recruitment_date_created = models.DateField(auto_now_add=True)
    recruitment_user_name = models.CharField(max_length=255, blank=True, null=True)
    recruitment_user_age = models.CharField(max_length=255, blank=True, null=True)
    recruitment_user_experience = models.CharField(max_length=255, blank=True, null=True)
    recruitment_user_last_company = models.CharField(max_length=255, blank=True, null=True)
    recruitment_user_last_education = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"NAME: {self.recruitment_name} | JOB TITLE: {self.recruitment_job_title} | PARTICIPANT {self.recruitment_user_name}"

    class Meta:
        indexes = [
            models.Index(fields=["recruitment_name"]),
            models.Index(fields=["id"]),
        ]
        verbose_name = "Recruitment"
        verbose_name_plural = "Recruitment"

