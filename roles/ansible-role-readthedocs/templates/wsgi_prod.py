"""WSGI application helper"""

from __future__ import absolute_import
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.prod")

from django.core.wsgi import get_wsgi_application  # pylint: disable=wrong-import-position
application = get_wsgi_application()
