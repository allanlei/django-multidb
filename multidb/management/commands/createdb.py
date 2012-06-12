from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from optparse import make_option

import logging
logger = logging.getLogger(__name__)

DEFAULT_DATABASE = settings.DATABASES['default']

class Command(BaseCommand):
    args = 'Database alias'
    help = 'Create a database'

    option_list = BaseCommand.option_list + (
        make_option('-e', '--engine', default=DEFAULT_DATABASE['ENGINE']),
        make_option('-n', '--name', default=DEFAULT_DATABASE['NAME']),
        make_option('-u', '--user', default=DEFAULT_DATABASE['USER']),
        make_option('--password', default=DEFAULT_DATABASE['PASSWORD']),
        make_option('-h','--host', default=DEFAULT_DATABASE['HOST']),
        make_option('-p', '--port', default=DEFAULT_DATABASE['PORT']),
    )
    
#    DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '%s/default.db' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}
        
    def handle(self, alias, **kwargs):
        print alias, kwargs
