from .base import *

DEBUG = True

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]

# SECRETS
secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

# DATABASE
# DATABASES = secrets['DATABASES']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS += [
    'django_extensions',
    # 'debug_toolbar',
]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# debug-toolbar
# INTERNAL_IPS = [
#     '127.0.0.1', 'localhost',
# ]

# STORAGE
# AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_REGION_NAME = 'ap-northeast-2'
# DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

# STATICFILES_STORAGE = 'config.storages.StaticStorage'
