"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from accounts.views import GoogleLogin, GoogleLoginCallback, LoginPage
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Route for the login page using the LoginPage view
    path("login/", LoginPage.as_view(), name="login"),

    # Add API Endpoint for token auth
    path("api/v1/auth/", include("dj_rest_auth.urls")),

    # Include the authentication URLs provided by allauth for account management
    re_path(r"^api/v1/auth/accounts/", include("allauth.urls")),

    # This should be added in front of registration
    re_path(
        "^api/v1/auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),

    # Include the registration URLs provided by dj-rest-auth
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),

    # Route for Google login authentication
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),

    # Route for the callback after Google authentication
    path(
        "api/v1/auth/google/callback/",
        GoogleLoginCallback.as_view(),
        name="google_login_callback",
    ),
]
