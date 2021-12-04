from .prod import *

DEBUG = True
SECRET_KEY = 'django-insecure-xfl@(vur%7&g!@9wn(rf0_2rtektuca^=1owsaaox2$p#r9yyn'
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
