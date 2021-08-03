import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH
sys.path.append('C:/Users/info/Documents/MGcoding/CRM')
sys.path.append('C:/Users/info/Documents/MGcoding/CRM/crmindigent')

os.environ['DJANGO_SETTINGS_MODULE'] = 'crmindigent.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crmindigent.settings')

application = get_wsgi_application()