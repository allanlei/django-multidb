from django.core.management.base import BaseCommand, CommandError, handle_default_options

import random
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        pass
        
        
#        MAX_CONNECTIONS = 60
#        
#        def restrict_max_connections(sender, connection, **kwargs):
#            dbs = connections.databases.keys()
#            if len(dbs) >= MAX_CONNECTIONS:
#                print 'clean'
#                db = dbs[random.randint(0, len(dbs) - 1)]       #Needs to be a smarter functions, ie based on idle time, can also clean up using cronjob
#                
#                while db == 'default' or connections[db] == connection:
#                    db = dbs[random.randint(0, len(dbs) - 1)]
#                connections[db].close()
#                del connections.databases[db]
#                    
#        connection_created.connect(restrict_max_connections)
#    
#    
#        tenants = ['database%s' % i for i in range(MAX_CONNECTIONS -MAX_CONNECTIONS + 3 - 1 - len(settings.DATABASES.keys()))]
#        
#        databases = 
#        for i in range(1000):
#            tenant = tenants[random.randint(0, len(tenants) - 1)]
#            settings.DATABASES[tenant] = settings.DATABASES['default'].copy()
#            print tenant, User.objects.using('default'), len(settings.DATABASES.keys())
        

##            
#        
##        
#        for i in range(50):
#            settings.DATABASES['db%s' % i] = settings.DATABASES['default'].copy()
##            print len(connections.all()), len(connections.databases.keys())

#        for db in settings.DATABASES.keys():
#            print User.objects.using(db)
#            connections.all().remove(connections[db])

#        print connections.all(), connections.databases.keys()
