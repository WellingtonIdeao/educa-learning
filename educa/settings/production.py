from .base import *

import environ

environ.Env.read_env()
env = environ.Env(
    DEBUG=(bool, False)
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ADMINS = (
    ('Wellington I', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}
