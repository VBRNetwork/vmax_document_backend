from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from dry_rest_permissions.generics import DRYPermissions
from .models import (
    HrFiles,
    HrFileRequest,
    RecruitmentLeads
)
from .serializers import (
    HrFilesSerializer,
    HrFileRequestSerializer,
    RecruitmentLeadsSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse


class HrFilesList(ListAPIView):
    queryset = HrFiles.objects.all()
    serializer_class = HrFilesSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class HrFileRequestCreateList(ListCreateAPIView):
    queryset = HrFileRequest.objects.all()
    serializer_class = HrFileRequestSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    def post(self, request, *args, **kwargs):

        user = request.user
        data = request.data
        save_request = (
            HrFileRequest(
                hr_request_user=user,
                hr_file_request_name=data['hr_file_request_name'],
                hr_file_request_date_created=data['hr_file_request_date_created'],
                hr_file_type=data['hr_file_type']
            )
        )
        save_request.save()
        return JsonResponse({"message": "Request saved successfully"}, status=201)

class RecruitmentLeadsCreateList(ListCreateAPIView):
    queryset = RecruitmentLeads.objects.all()
    serializer_class = RecruitmentLeadsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class RecruitmentLeadsRetreiveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = RecruitmentLeads.objects.all()
    serializer_class = RecruitmentLeadsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class RecruitmentLeadsListCreateAPIView(ListCreateAPIView):
    queryset = RecruitmentLeads.objects.all()
    serializer_class = RecruitmentLeadsSerializer
    permission_classes = [AllowAny]
    pagination_class = None