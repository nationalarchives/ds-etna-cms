import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-o%^&(+gnj0*f0q0%a9xf+l-_88^7jqgavz#_9p6p$u8n#9kh72"
)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = "/media"


WAGTAILADMIN_BASE_URL = os.getenv(
    "WAGTAILADMIN_BASE_URL", "http://localhost:65533"
)
WAGTAIL_HEADLESS_PREVIEW = {
    "CLIENT_URLS": {
        "default": "http://localhost:65535/preview",
    },
    "SERVE_BASE_URL": "http://localhost:65535",
    "REDIRECT_ON_PREVIEW": False,
    "ENFORCE_TRAILING_SLASH": True,
}

try:
    from .local import *
except ImportError:
    pass
