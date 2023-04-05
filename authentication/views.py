from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_auth.serializers import LoginSerializer

from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

from rest_auth.app_settings import TokenSerializer, JWTSerializer, create_token
from rest_auth.models import TokenModel
from rest_auth.utils import jwt_encode
import requests

from .serializers import RegisterSerializer

from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from .providers.google.views import GoogleOAuth2RestAdapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.microsoft.views import MicrosoftGraphOAuth2Adapter

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("password1", "password2")
)


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.SITE_PROTOCOL + settings.SITE_DOMAIN
    client_class = OAuth2Client

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2RestAdapter
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
class MicrosoftLogin(SocialLoginView):

    adapter_class = MicrosoftGraphOAuth2Adapter
    callback_url = "http://localhost:8080/auth/login"
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer


    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class LoginView(GenericAPIView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework
    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def get_response_serializer(self):
        return (
            JWTSerializer
            if getattr(settings, "REST_USE_JWT", False)
            else TokenSerializer
        )

    def login(self):
        self.user = self.serializer.validated_data["user"]

        if getattr(settings, "REST_USE_JWT", False):
            self.token = jwt_encode(self.user)
        else:
            self.token = create_token(
                self.token_model, self.user, self.serializer
            )

        if self.user.otp_enabled:
            self.otp = tmp_user_id(self.user.id)
        elif not getattr(self.user, "otp", False):
            create_otp(self.user, self.user.username)

        if getattr(settings, "REST_SESSION_LOGIN", True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if self.user.otp_enabled:
            return Response(
                {"otp": True, "user_id": self.otp["otp"]},
                status=status.HTTP_200_OK,
            )

        if getattr(settings, "REST_USE_JWT", False):
            data = {"user": self.user, "token": self.token}
            serializer = serializer_class(
                instance=data, context={"request": self.request}
            )
        else:
            serializer = serializer_class(
                instance=self.token, context={"request": self.request}
            )

        response = Response(serializer.data, status=status.HTTP_200_OK)
        if getattr(settings, "REST_USE_JWT", False):
            from rest_framework_jwt.settings import (
                api_settings as jwt_settings,
            )

            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime

                expiration = (
                    datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
                )
                response.set_cookie(
                    jwt_settings.JWT_AUTH_COOKIE,
                    self.token,
                    expires=expiration,
                    httponly=True,
                )
        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class RegisterView(CreateAPIView):
    from rest_auth.registration.app_settings import (
        register_permission_classes,
    )

    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if (
            allauth_settings.EMAIL_VERIFICATION
            == allauth_settings.EmailVerificationMethod.MANDATORY
        ):
            return {"detail": _("Verification e-mail sent.")}

        if not getattr(settings, "REST_USE_JWT", False):
            return TokenSerializer(user.auth_token).data

        data = {"user": user, "token": self.token}
        return JWTSerializer(data).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = Response(
            self.get_response_data(user),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

        if getattr(settings, "REST_USE_JWT", False):
            from rest_framework_jwt.settings import (
                api_settings as jwt_settings,
            )

            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime

                expiration = (
                    datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
                )
                response.set_cookie(
                    jwt_settings.JWT_AUTH_COOKIE,
                    self.token,
                    expires=expiration,
                    httponly=True,
                )
        return response

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, "REST_USE_JWT", False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(
            self.request._request,
            user,
            allauth_settings.EMAIL_VERIFICATION,
            None,
        )
        return user

    def get_response_serializer(self):
        return (
            JWTSerializer
            if getattr(settings, "REST_USE_JWT", False)
            else TokenSerializer
        )
