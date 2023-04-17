import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '1231hj23i1hn23ui1g2uy3g2u7ydfhsofguy9' # local

DEBUG = True # local

ALLOWED_HOSTS = ['bloknot-ik.ru', '77.220.141.41', '127.0.0.1', 'localhost'] # local
#ALLOWED_HOSTS = []


DJANGO_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

PROJECT_APPS = [

    'base',
    'analytics',
    'app',
    'user',

]

THIRD_PARTY_APPS = [

    'compressor',
    'tinymce',

]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

print(INSTALLED_APPS)

""" 
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (

    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',

) """

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend', # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
  
    'social_core.backends.yandex.YandexOAuth2', # бекенд авторизации через Яндекс
    'social_core.backends.vk.VKOAuth2', # бекенд авторизации через ВКонтакте
) 

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            
            ],
        
        },
    
    },

]

WSGI_APPLICATION = 'web.wsgi.application'

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow' # local

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# scss

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

# email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True # local
#EMAIL_HOST_USER = 'kosyakovsn@gmail.com'
#EMAIL_HOST_PASSWORD = 'gigharagfknceknq' # local
#DEFkosyakovsn AULT_FROM_EMAIL = 'bloknotikk@gmail.com'


SOCIAL_AUTH_VK_OAUTH2_KEY = '51609135'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'RsKt6CO0oSR4efHeiLQr'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = '93639dbecb764e2aae0f55b67b416e61'
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = '37f59f3dc19b4d53bf51c931c1baf09b'

