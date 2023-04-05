from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from dry_rest_permissions.generics import DRYPermissions
from .serializers import (
    VbrContractsSerializer,
    VbrPartnersSerializer,
    VbrDocumentsSerializer,
    DocumentsSerializer,
    CompanyLocationsSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    VbrPartners,
    VbrContracts,
    VbrDocuments,
    Documents,
    CompanyLocations,
)



class CompanyLocationsListAPIView(ListAPIView):
    queryset = CompanyLocations.objects.all()
    serializer_class = CompanyLocationsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class DocumentsListCreateAPIView(ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class DocumentListRomexpoListAPIView(ListAPIView):
    queryset = Documents.objects.filter(location__location_name="Romexpo")
    serializer_class = DocumentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class DocumentListClujListAPIView(ListAPIView):
    queryset = Documents.objects.filter(location__location_name="Cluj")
    serializer_class = DocumentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class DocumentListTitanListAPIView(ListAPIView):
    queryset = Documents.objects.filter(location__location_name="Titan")
    serializer_class = DocumentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class VbrPartnersList(ListCreateAPIView):
    queryset = VbrPartners.objects.all()
    serializer_class = VbrPartnersSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class VbrPartnersUpdate(RetrieveUpdateAPIView):
    queryset = VbrPartners.objects.all()
    serializer_class = VbrPartnersSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class VbrDocumentsList(ListCreateAPIView):
    serializer_class = VbrDocumentsSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    queryset = VbrDocuments.objects.all()


class VbrContractsList(ListCreateAPIView):
    serializer_class = VbrContractsSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    queryset = VbrContracts.objects.all()


class VbrPartnersList(ListCreateAPIView):
    queryset = VbrPartners.objects.all()
    serializer_class = VbrPartnersSerializer
    permission_classes = [AllowAny]
    pagination_class = None
