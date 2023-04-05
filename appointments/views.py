from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from dry_rest_permissions.generics import DRYPermissions
from .models import (
    Appointments,
)
from .serializers import (
    AppointmentsSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse


class AppointmentsCreateList(ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    def post(self, request, *args, **kwargs):

        user = request.user
        data = request.data
        save_request = (
            Appointments(
                appointment_customer=user,
                appointment_title=data['appointment_title'],
                appointment_description=data['appointment_description'],
                appointment_date=data['appointment_date'],
                appointment_duration=data['appointment_duration'],
                appointment_room=data['appointment_room'],
            )
        )
        save_request.save()
        return JsonResponse({"message": "Request saved successfully"}, status=201)