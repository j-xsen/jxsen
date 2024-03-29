"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys
import traceback
import signal
import time

from django.core.wsgi import get_wsgi_application
import project.settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

try:
    application = get_wsgi_application()
    print("WSGI without exception")
except Exception:
    print("Handling WSGI Exception")
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
