# surveyhub/settings/prod.py
from .base import *

import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}



DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
    "foxxelabs.com",           # your custom domain
    "www.foxxelabs.com",       # (optional, if you use www)
    "your-app-name.railway.app" # (for Railway deployment, update as needed)
]


# Database (example: using dj-database-url for Railway or other PaaS)
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

# Static files (served by WhiteNoise or PaaS)
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SECURE_HSTS_SECONDS = 31536000 
#SECURE_SSL_REDIRECT = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@foxxelabs.com"
