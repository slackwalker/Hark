import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'hark.production_settings'

sys.path.append('/home/sleeper/projects')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
