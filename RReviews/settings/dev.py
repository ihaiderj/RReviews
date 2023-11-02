from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2u2wwpgj5y6s17e6&)fypx$iop=0i^11yz6%1yg5v^)^r_qrhi'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [

    'debug_toolbar',

]

MIDDLEWARE = MIDDLEWARE + [
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   
]




INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

try:
    from .local import *
except ImportError:
    pass
