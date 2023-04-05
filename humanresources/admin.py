from django.contrib import admin
from .models import HrFiles, HrFileRequest, RecruitmentLeads

admin.site.register(HrFiles)
admin.site.register(HrFileRequest)
admin.site.register(RecruitmentLeads)
