from .base import *

DEBUG = False

# SECRETS
secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

# DATABASE
DATABASES = secrets['DATABASES']