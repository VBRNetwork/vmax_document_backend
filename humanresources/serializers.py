from rest_framework import serializers
from .models import (
    HrFiles,
    HrFileRequest,
    RecruitmentLeads
)
from users.serializers import UserSerializer
from dry_rest_permissions.generics import DRYPermissionsField


class HrFilesSerializer(serializers.ModelSerializer):
    hr_file_user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = HrFiles
        fields = "__all__"

class HrFileRequestSerializer(serializers.ModelSerializer):
    hr_request_user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = HrFileRequest
        fields = "__all__"

class RecruitmentLeadsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecruitmentLeads
        fields = "__all__"
