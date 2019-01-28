#! -*- coding: utf-8 -*-


# author: forcemain@163.com


"""
Django settings for entrance project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


import os


from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f906dq+$$7njkgf)w&rgq+mspu%$yf-@_+t49&!qz2oa51e0d5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_URL = reverse_lazy('cas_app:user-login')

# Application definition

CUSTOMIZED_APPS = [
    'entrance',
    'cas_app',
    'smn_app',
]

INSTALLED_APPS = CUSTOMIZED_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = INSTALLED_APPS + [
    'rest_framework',
    'rest_framework.authtoken',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'entrance.urls'

AUTH_USER_MODEL = 'cas_app.User'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'entrance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
_STATIC_BASE = os.path.join(BASE_DIR, 'static')
_STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'
STATIC_ROOT = _STATIC_ROOT if isinstance(_STATIC_ROOT, unicode) else _STATIC_ROOT.decode('utf-8')
STATIC_BASE = _STATIC_BASE if isinstance(_STATIC_BASE, unicode) else _STATIC_BASE.decode('utf-8')
STATICFILES_DIRS = (_STATIC_BASE,)


# Media files
_MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')
MEDIA_URL = '/medias/'
MEDIA_ROOT = _MEDIA_ROOT if isinstance(_MEDIA_ROOT, unicode) else _MEDIA_ROOT.decode('utf-8')


# Rest framework
REST_FRAMEWORK = {
    'PAGINATE_BY': 15,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'utils.rest.exps_handler.drf_exception_handler',
}
REST_FRAMEWORK_AUTH_TOKEN_EXPIRE_MINUTES = None


# Rest exception
FRIENDLY_ERRORS = {
    'CATCH_ALL_EXCEPTIONS': False,
}


# Weixin
WEIXIN_AGENTID = 0
WEIXIN_SECRET = ''
WEIXIN_CORPID = ''
WEIXIN_CODE_URL = 'https://open.work.weixin.qq.com/wwopen/sso/qrConnect'
WEIXIN_USERINFO_URL = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo'
WEIXIN_ACCESS_TOKEN_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'


# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'utils.core.auth.weixin.WeixinQcodeRemoteUserBackend',
]
