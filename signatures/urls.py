from django.conf.urls import url
from .views import SignatureCreateView


urlpatterns = [
    url(
        r"signature/$",
        SignatureCreateView.as_view(),
        name="signature",
    ),
]
