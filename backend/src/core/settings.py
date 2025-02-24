"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from dotenv import load_dotenv
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load env from parent path
ENV_DIR = os.path.join(BASE_DIR, "..", ".env")
load_dotenv(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$k0f0!qp@0k%1xa_)zy!+xvwpv)+&$q&!d69ma@l615bdc2ytd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Required by django-allauth for managing site-specific data,
    # such as site domains and configurations.
    'django.contrib.sites',

    # Core Django Rest Framework (DRF) package that provides tools
    # to build APIs and handle request/response data in various formats (JSON, XML, etc.).
    'rest_framework',

    # Enables token-based authentication in DRF, allowing users
    # to authenticate using tokens.
    'rest_framework.authtoken',


    # A Django app that integrates dj-rest-auth with Django-allauth,
    # providing authentication and registration endpoints for RESTful APIs.
    'dj_rest_auth',

    # Provides JWT authentication support for Django REST Framework,
    # allowing for secure token-based authentication using JSON Web Tokens.
    'rest_framework_simplejwt',

    # Django-allauth package, which provides comprehensive user authentication,
    # registration, and account management.
    'allauth',

    # A submodule of django-allauth that handles user account registration,
    # login, password management, and more.
    'allauth.account',

    # Extends allauth to support social authentication
    # (e.g., logging in with Facebook, Google, etc.).
    'allauth.socialaccount',

    # Adds user registration endpoints to dj-rest-auth, enabling JWT-based
    # user registration and management (e.g., email verification, password reset).
    'dj_rest_auth.registration',

    # Support login with Google
    'allauth.socialaccount.providers.google',

    'accounts'

]

# The ID of the site that this Django project is associated with.
# This is required for django.contrib.sites and django-allauth to work correctly. SITE_ID = 1
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware for django-allauth that manages account-related operations,
    # such as handling user sessions and account state.
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JWTCookieAuthentication vs JWTAuthentication
#
# JWTAuthentication:
# - JWTAuthentication uses access tokens passed in the Authorization header.
# - The token must be included in every request under the "Authorization" header, typically in the form "Bearer <token>".
# - It is suitable for stateless API communication where cookies are not involved.
# - It requires clients (like frontend apps) to store tokens and add them to the header with each request.
#
# JWTCookieAuthentication:
# - JWTCookieAuthentication, often part of dj-rest-auth or custom middleware, uses cookies to store JWT tokens (both access and refresh).
# - Tokens are automatically included in the request by the browser (as cookies) without needing to manually add them to headers.
# - It is more user-friendly in web-based apps as tokens are stored and sent securely via cookies (especially HTTPOnly cookies).
# - This authentication method can simplify frontend development as cookies are handled natively by browsers.

# Basic Usage Example:
# In the following configuration, JWTAuthentication is being used, meaning JWT tokens must be included in the request header.

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# djangorestframework-simplejwt settings

from datetime import timedelta

# Duration for which the access token is valid
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),

    # Duration for which the refresh token is valid
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# REST authentication settings for JWT usage
REST_AUTH = {
    # Use JWT for authentication
    "USE_JWT": True,

    # Do not send the access token as a cookie
    # "JWT_AUTH_COOKIE": "_auth",

    # Do not send the refresh token as a cookie
    # "JWT_AUTH_REFRESH_COOKIE": "_refresh",

    # Ensure the refresh token is sent with the request
    "JWT_AUTH_HTTPONLY": False,
}

# Email settings
# The authentication method for user accounts, set to "email"
# to require email/password for login.
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Whether a username is required for user accounts; set to False
# to allow authentication solely using email.
ACCOUNT_USERNAME_REQUIRED = False

# Whether an email is required for user accounts; set to True
# to ensure users must provide an email address during registration.
ACCOUNT_EMAIL_REQUIRED = True

# The email verification method; set to "none" to disable
# email verification after registration.
ACCOUNT_EMAIL_VERIFICATION = "none"

# Django SMTP email configuration.
# Specifies the backend used for sending emails.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# The SMTP server host used to send emails.
EMAIL_HOST = os.getenv("EMAIL_HOST")

# The SMTP server port for sending emails; typically 587 for TLS.
EMAIL_PORT = os.getenv("EMAIL_PORT")

# Whether to use TLS or SSL when connecting to the SMTP server.
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# The email address used to send emails (SMTP authentication user).
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

# The password or app-specific password for the email sending address.
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")

# Requires users to verify their email address after registration.
# Registration is incomplete until the email is confirmed.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Allows users to confirm their email by clicking the confirmation link in the GET request.
# No need to send a separate POST request to confirm the email.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# The URL path where users are redirected after a successful email verification.
# In this case, it redirects users to the admin login page.
LOGIN_URL = "/admin"

import os

# The URL to redirect to after a successful email confirmation for anonymous users.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = os.environ.get(
    "EMAIL_CONFIRM_REDIRECT_URL", "https://myapp.com/login"
)

# The URL to redirect to after a successful email confirmation for authenticated users.
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = os.environ.get(
    "EMAIL_CONFIRM_REDIRECT_URL", "https://myapp.com/login"
)

# Google OAuth
GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_OAUTH_CALLBACK_URL = os.getenv("GOOGLE_OAUTH_CALLBACK_URL")

# django-allauth (social) configuration for social authentication
# Enable email authentication for social accounts
# This setting checks if a local account exists with the email address provided by the social authentication provider.
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True

# Automatically connect the social account to the existing local account if the email address matches
# This helps to seamlessly link users' social accounts with their local accounts, enhancing user experience.
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

# Configuration for social authentication providers
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # List of applications using Google OAuth
        "APPS": [
            {
                # Client ID provided by Google API console for OAuth authentication
                "client_id": GOOGLE_OAUTH_CLIENT_ID,
                # Client secret provided by Google API console for OAuth authentication
                "secret": GOOGLE_OAUTH_CLIENT_SECRET,
                # Additional key, if needed (left empty for now)
                "key": "",
            },
        ],
        # Define the scopes requested from Google
        # These scopes determine what information we can access from the user's Google account
        "SCOPE": ["profile", "email"],
        # Authentication parameters for the OAuth request
        "AUTH_PARAMS": {
            # Set access type to online to request access to the user's account
            "access_type": "online",
        },
    }
}