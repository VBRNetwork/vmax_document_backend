from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Signature
from .serializers import SignatureSerializer

# Create your views here.
class SignatureCreateView(CreateAPIView):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
    permission_classes = [IsAuthenticated]
