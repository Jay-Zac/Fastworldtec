from pathlib import Path  # Import Path class for path operations

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Define the base directory of the project

# SECURITY WARNING: keep the secret key used in production secret! Secret key for cryptographic operations
SECRET_KEY = 'django-insecure-$5!nvt8*m_72m2i#bvwlusi*bqm47%(fe+q^96p_#+k2ev6but'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Debug mode toggle (set to False in production)

ALLOWED_HOSTS = []  # List of allowed hosts for the application

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin app
    'django.contrib.auth',  # Django authentication app
    'django.contrib.contenttypes',  # Django content types app
    'django.contrib.sessions',  # Django sessions app
    'django.contrib.messages',  # Django messages app
    'django.contrib.staticfiles',  # Django static files app

    # local apps
    'homepage.apps.HomepageConfig',  # Local app: Homepage
    'courses.apps.CoursesConfig',  # Local app: Courses
    'software.apps.SoftwareConfig',  # Local app: Software
    'themes.apps.ThemesConfig',  # Local app: Themes
    'tools.apps.ToolsConfig',  # Local app: Tools
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection middleware
]

ROOT_URLCONF = 'Fastworldtec.urls'  # Root URL configuration module

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template backend
        'DIRS': [BASE_DIR / 'templates', ],  # Directories to search for templates
        'APP_DIRS': True,  # Whether to look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Messages context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'Fastworldtec.wsgi.application'  # WSGI application module

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Database engine (MySQL)
        'NAME': 'fastworldtec_database',  # Name of the database
        'HOST': 'localhost',  # Database host
        'PORT': '3306',  # Database port
        'USER': 'root',  # Database user
        'PASSWORD': 'jayzac',  # Database password
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # Validator for attribute similarity
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validator for minimum length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validator for common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validator for numeric passwords
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'  # Default language code

TIME_ZONE = 'Africa/Nairobi'  # Default time zone

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable timezone-aware datetime

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'  # URL prefix for static files
STATIC_ROOT = BASE_DIR / 'static'  # Directory to collect static files

STATICFILES_DIRS = ['static/local_static/', ]  # Additional directories to look for static files

MEDIA_URL = 'media/'  # URL prefix for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory to store media files

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default field type for auto-created primary keys
