"""
script that sets up the Django web framework for running an application
in a web server using the WSGI (Web Server Gateway Interface) protocol
"""

import os
from django.core.wsgi import get_wsgi_application
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("SETTINGS"))

application = get_wsgi_application()
