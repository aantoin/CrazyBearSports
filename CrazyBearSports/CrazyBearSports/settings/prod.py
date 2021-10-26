"""Settings for production"""
import os
from .base import * # pylint: disable=wildcard-import,unused-wildcard-import

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','64.227.15.207', 'crazybearsports.com','www.crazybearsports.com']
