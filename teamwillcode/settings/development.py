from .base import *
import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS =['static/']
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DB_PATH = os.path.join(ROOT_DIR, '.config', 'db.json')
database = json.loads(open(SECRETS_PATH).read())

for key, value in database.items():
    setattr(sys.modules[__name__], key, value)

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '****',
#         'USER': '****',
#         'PASSWORD': '****',
#         'HOST': '****',
#         'PORT': '****',
#     }
# }