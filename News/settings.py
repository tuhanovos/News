"""
Django settings for News project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g(xkyp0i+*pyhhr(acl$31zmm0-pl=@m+#kwu9ioo%xsn@1t=&'

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
    'django.contrib.sites',
    'blog.apps.BlogConfig',
    'bootstrap4',
    'menu',
    'ckeditor',
    'ckeditor_uploader',
    'dbbackup',
    # 'rest_framework',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.facebook',
    ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'News.urls'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 60
LOGIN_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = [
    # 'News.EmailAuthBackend.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'blog/templates')]
        ,
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

WSGI_APPLICATION = 'News.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newsdb',
        'USER': 'tuhanovos',
        'PASSWORD': '0308198O',
    }
}


# Настройки резервной копии базы данных

# DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backup-db')}

DBBACKUP_CONNECTORS = {
    'default': {
        'USER': 'tuhanovos',
        'PASSWORD': '0308198O',
        'HOST': 'localhost'
    }
}

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR + 'static')

# Настройки тестового редактора ckeditor

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'

# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

MEDIA_ROOT = os.path.join(BASE_DIR + '/media/')
MEDIA_URL = '/media/'
# CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
# CKEDITOR_RESTRICT_BY_USER = True
# CKEDITOR_BROWSE_SHOW_DIRS = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

CKEDITOR_CONFIGS = {
    'default': {

        'skin': 'moono',

        # 'skin': 'office2013',

        'toolbar_Basic': [

            ['Source', '-', 'Bold', 'Italic']

        ],

        'toolbar_YourCustomToolbarConfig': [

            {'name': 'document', 'items': ['Source', '-', '-', 'NewPage', 'Preview', 'Print', '-', 'Templates']},

            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},

            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},

            # {'name': 'forms',
            #
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #
            #            'HiddenField']},

            '/',

            {'name': 'basicstyles',

             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},

            {'name': 'paragraph',

             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',

                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',

                       'Language']},

            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},

            {'name': 'insert',

             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},

            '/',

            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},

            {'name': 'colors', 'items': ['TextColor', 'BGColor']},

            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},

            {'name': 'about', 'items': ['About']},

            '/',  # put this to force next toolbar on new line

            {'name': 'yourcustomtools', 'items': [

                # put the name of your editor.ui.addButton here

                'Preview',

                'Maximize',

            ]},

        ],

        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here

        # 'toolbarGroups': [{ ‘name’: ‘document’, ‘groups’: [ 'mode', 'document', 'doctools' ] }],

        # 'height': 291,

        'width': '100%',

        # 'filebrowserWindowHeight': 725,

        # 'filebrowserWindowWidth': 940,

        # 'toolbarCanCollapse': True,

        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',

        'tabSpaces': 4,

        'removePlugins': 'stylesheetparser',

        'extraPlugins': ','.join(

            [

                # your extra plugins here

                'div',

                'autolink',

                'autoembed',

                'embedsemantic',

                'autogrow',

                # 'devtools',

                'widget',

                'lineutils',

                'clipboard',

                'dialog',

                'dialogui',

                'elementspath',

                'codesnippet'

            ]),

    }

}


