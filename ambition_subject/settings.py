"""
Django settings for ambition_subject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = 'ambition_subject'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jwggbn11gw22h6&0n@q0t97e)&)pg^n_*$18xj350f0%w+ywba'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_sync.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'ambition_subject.apps.EdcBaseAppConfig',
    'ambition_subject.apps.EdcBaseTestAppConfig',
    'ambition_subject.apps.EdcLabAppConfig',
    'ambition_subject.apps.EdcLabelAppConfig',
    'ambition_subject.apps.EdcMetadataAppConfig',
    'ambition_subject.apps.EdcIdentifierAppConfig',
    'ambition_subject.apps.EdcProtocolAppConfig',
    'ambition_subject.apps.EdcConsentAppConfig',
    'ambition_subject.apps.EdcDeviceAppConfig',
    'ambition_subject.apps.EdcTimepointAppConfig',
    'ambition_subject.apps.EdcAppointmentAppConfig',
    'ambition_subject.apps.EdcVisitTrackingAppConfig',
    'ambition_subject.apps.AppConfig',
    'ambition_screening.apps.AppConfig',
    'ambition_subject_validators.apps.AppConfig',
    'ambition_labs.apps.AppConfig',
    'ambition_reference.apps.AppConfig',
    'ambition_metadata_rules.apps.AppConfig',
    'ambition_visit_schedule.apps.AppConfig',
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

ROOT_URLCONF = 'ambition_subject.urls'

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

WSGI_APPLICATION = 'ambition_subject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'ambition_subject', 'static')
STATIC_URL = '/static/'
DEVICE_ID = '99'
EDC_LAB_REQUISITION_MODEL = 'ambition_subject.subjectrequisition'
# DEVICE_ROLE = 'CentralServer'
KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')
GIT_DIR = BASE_DIR

if 'test' in sys.argv and 'mysql' not in DATABASES.get('default').get('ENGINE'):
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        "edc_call_manager": None,
        "edc_appointment": None,
        "edc_call_manager": None,
        "edc_consent": None,
        "edc_death_report": None,
        "edc_export": None,
        "edc_identifier": None,
        "edc_lab": None,
        "edc_metadata": None,
        "edc_rule_groups": None,
        "edc_reference": None,
        "edc_registration": None,
        "edc_sync_files": None,
        "edc_sync": None,
        "ambition_subject": None,
        "ambition_screening": None}
