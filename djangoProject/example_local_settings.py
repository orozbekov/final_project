# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(uu+i0kejrxbu#ti@zmhl2d8w%d#^724%)1=#73b3c2+3&md3p'

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}