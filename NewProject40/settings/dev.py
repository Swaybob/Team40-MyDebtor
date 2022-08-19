from .common import *
from decouple import Config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g%u0@r(y@racy6emq_n(shu(g%zmcrs5vu(!pn=8*pm+2=yc28'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  config('NAME'),  
        'HOST': config('HOST'), 
        'USER': 'root',
        'PASSWORD': config('PASSWORD'), 
        'PORT': config('PORT'),
    }
}
