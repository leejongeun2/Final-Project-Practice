"""
Django settings for pjt project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'pjt/secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

# SECURITY WARNING: keep the secret key used in production secret!
def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1", 
    "localhost",
    "zugzog-env.eba-gsmmen2n.ap-northeast-2.elasticbeanstalk.com",
]


# Application definition

INSTALLED_APPS = [
    'accounts',
    'reviews',
    'products',
    'storages',
    'imagekit',
    'django_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'pjt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'pjt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# static
# STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 로고와 같이 고정적으로 삽입하는 정적 이미지, 오류 발생
STATIC_URL = '/static/' # 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] # 이곳에 지정한 경로에 모든 파일을 모은다.



# image
# MEDIA_ROOT = BASE_DIR / 'images' # 업로드가 끝난 파일을 배치할 최상위 경로를 지정하는 설정 항목
# MEDIA_URL = '/media/' # 웹 페이지에서 사용할 이미지 파일의 최상위 URL 경로


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

# AWS_REGION = "ap-northeast-2"
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
#     AWS_STORAGE_BUCKET_NAME,
#     AWS_REGION,
# )


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "zugzog", # 코드 블럭 아래 이미지 참고하여 입력
#         "USER": "postgres",
#         "PASSWORD": "whddms95", # 데이터베이스 생성 시 작성한 패스워드
#         "HOST": "zugzog.crrwkbgnpdyb.ap-northeast-2.rds.amazonaws.com", # 코드 블럭 아래 이미지 참고하여 입력
#         "PORT": "5432",
#     }
# }



DEBUG = os.getenv("DEBUG") == "True"
if DEBUG: 
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:   
    # DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "pjt.storages.MediaStorage"
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"), # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"), # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"), # .env 파일에 value 작성
            "PORT": "5432",
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # 64비트보다 더 큰 정수값을 사용하고 싶을 때 모델에 각 정의해주는 것보다 여기서 전역에 적용되도록 기재함

AUTH_USER_MODEL = "accounts.User" #  User를 나타내는데 사용하는 모델을 accounts 앱의 커스터마이징한 user모델임을 정의해줌


