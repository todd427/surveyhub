# surveyhub/settings/dev.py
from .base import *

DEBUG = True
SECRET_KEY = "your-insecure-dev-key"

ALLOWED_HOSTS = []

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
