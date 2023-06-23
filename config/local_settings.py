from pathlib import Path
from config.settings import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2hfgm=hhc$r1qje#36i1j&!*furr%p9nf02#$5d5o_-0l)s5-b'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Celery Configuration Options
# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

# Websocket settings
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}