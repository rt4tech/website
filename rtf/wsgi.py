from os import sep
from os import environ
from os.path import abspath, dirname

PROJECT_DIR = dirname(abspath(__file__))
settings_module = "%s.settings" % PROJECT_DIR.split(sep)[-1]
environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
