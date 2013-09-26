from os import sep
from os.environ import setdefault
from os.path import abspath, dirname
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(abspath(__file__))
settings_module = "%s.settings" % PROJECT_DIR.split(sep)[-1]
setdefault("DJANGO_SETTINGS_MODULE", settings_module)
application = get_wsgi_application()
