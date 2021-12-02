from .prod import *

# DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'goodsshop',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
        'HOST': 'db',
        # 'HOST': '127.0.0.1',
        # 'PORT': '54321',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'nginx', 'static')
