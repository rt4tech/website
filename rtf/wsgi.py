from os import sep
from os.path import abspath, dirname

PROJECT_ROOT = dirname(abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
