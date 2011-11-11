from django.core.management.base import BaseCommand, CommandError

from optparse import make_option

import random
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = 'create, delete, info'
    help = 'Multidb management'

    option_list = BaseCommand.option_list + (
#        make_option('--delete', action='store_true', dest='delete', default=False, help='Delete poll instead of closing it'),
    )
        
    def handle(self, subcommand, **kwargs):
        if subcommand == 'create':
            return self.create(**kwargs)
        elif subcommand == 'delete':
            return self.delete(**kwargs)
        elif subcommand == 'info':
            return self.info(**kwargs)
        raise CommandError('Unknown subcommand %s' % subcommand)

    def create(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    def info(self, **kwargs):
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
