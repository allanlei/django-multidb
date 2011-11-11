from django.utils import unittest
from django.db import connections
from django.conf import settings
from django.core.management import call_command
from django.db.backends.signals import connection_created
from django.contrib.auth.models import User

from multidb.signals import limit_max_connections, track_connection_order
from multidb.settings import MULTIDB_MAX_CONNECTIONS

import random
import string

def random_string(length=5):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(length))


class MultiDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        connection_created.connect(track_connection_order)
        connection_created.connect(limit_max_connections)
        
        test_databases = (MULTIDB_MAX_CONNECTIONS - len(settings.DATABASES.keys())) * 2
        databases = []
        
        while len(databases) < test_databases:
            db = '%s.com' % random_string()
            while db in databases:
                db = '%s.com' % random_string()
            databases.append(db)
        
        self.databases = databases
        for alias in self.databases:
            db_settings = settings.DATABASES['default'].copy()
            db_settings['NAME'] = 'databases/%s.db' % alias
            settings.DATABASES[alias] = db_settings
            print 'Syncing %s' % alias
            call_command('syncdb', database=alias, interactive=False, verbosity=0)
        print 'Setup Done.'
        print 'settings.DATABASES: %s' % len(settings.DATABASES.keys())
        print 'connections.databases: %s' % len(connections.databases.keys())
        print 'connections: %s' % len(connections.all())
        
        
    def write(self, amount=1000):
        for i in range(amount):
            alias = random.choice(self.databases)
            self.writeOne(alias)

    def writeOne(self, alias):
        if alias not in settings.DATABASES:
            db_settings = settings.DATABASES['default'].copy()
            db_settings['NAME'] = 'databases/%s.db' % alias
            settings.DATABASES[alias] = db_settings
        print 'Write to %s %s' % (alias, alias in settings.DATABASES)
        username = random_string()
        while User.objects.using(alias).filter(username=username).exists():
            username = random_string()
        return User.objects.using(alias).create(username=username)

    def testWrite10(self):
        self.write(1000)

#    def testWrite100(self):
#        self.write(100)

#    def testWrite1000(self):
#        self.write(1000)
