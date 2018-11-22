from .base import *

DEBUG = False

# SECRETS
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

# ALLOWED_HOSTS
ALLOWED_HOSTS = [
    "backends.xyz",
    "www.backends.xyz",
    "api.backends.xyz",
    ".elasticbeanstalk.com",
    "localhost",
]

# DATABASE
DATABASES = secrets['DATABASES']

# STORAGE
AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
