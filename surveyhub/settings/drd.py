import os
from dotenv import load_dotenv
import dj_database_url
from .base import *

# Go two levels up from settings/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # surveyhub/
dotenv_file = os.environ.get("DJANGO_ENV_FILE", ".env.drd")
dotenv_path = os.path.join(BASE_DIR, dotenv_file)
print("Looking for dotenv at:", dotenv_path)
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is not set!")

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)
}
print("DATABASES", DATABASES)
DEBUG = True

ALLOWED_HOSTS = [
    "localhost", "127.0.0.1", "[::1]", "foxxelabs.com", "www.foxxelabs.com", "your-app-name.railway.app"
]

# ... (rest of your settings)
