import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("db_name"),
        'USER': os.getenv("db_user"),
        'PASSWORD': os.getenv("db_password"),
        'HOST': os.getenv("db_host"),
        'PORT': os.getenv("db_port"),
    }
}
