from django.conf.urls import url
from django.urls import include, path
from .views import (
    VbrPartnersList,
    VbrContractsList,
    VbrPartnersUpdate,
    DocumentsListCreateAPIView,
    CompanyLocationsListAPIView,
    DocumentListRomexpoListAPIView,
    DocumentListClujListAPIView,
    DocumentListTitanListAPIView,
)


urlpatterns = [
    url(
        r"partners/$",
        VbrPartnersList.as_view(),
        name="partners",
    ),
    url(
        r"partners/update/(?P<pk>\d+)$",
        VbrPartnersUpdate.as_view(),
        name="partners_update",
    ),
    url(
        r"contracts/$",
        VbrContractsList.as_view(),
        name="contracts",
    ),
    url(
        r"documents/$",
        DocumentsListCreateAPIView.as_view(),
        name="documents",
    ),
    url(
        r"contracts/(?P<contract_id>\d+)$",
        VbrContractsList.as_view(),
        name="contracts",
    ),
    url(
        r"locations/$",
        CompanyLocationsListAPIView.as_view(),
        name="locations",
    ),
    url(
        r"documents/romexpo/$",
        DocumentListRomexpoListAPIView.as_view(),
        name="documents_romexpo",
    ),
    url(
        r"documents/cluj/$",
        DocumentListClujListAPIView.as_view(),
        name="documents_cluj",
    ),
    url(
        r"documents/titan/$",
        DocumentListTitanListAPIView.as_view(),
        name="documents_titan",
    ),
]
