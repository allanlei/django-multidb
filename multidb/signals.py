from django.db import connections
#from django.dispatch import Signal
from django.core.urlresolvers import get_callable
from django.core.cache import cache

from multidb.settings import MULTIDB_MAX_CONNECTIONS, MULTIDB_MAX_CONNECTIONS_MAPPING, MULTIDB_CLEANUP_FUNCTION, MULTIDB_EXCLUDE_FROM_CLEANUP, MULTIDB_ALLOW_CURRENT_CONNECTION_CLEANUP
from multidb import utils

from sets import Set
import logging
logger = logging.getLogger(__name__)


cleanup = get_callable(MULTIDB_CLEANUP_FUNCTION)

def track_connection_order(sender, connection, **kwargs):
    connected_alias = None
    for alias, conn in connections._connections.items():
        if conn == connection:
            connected_alias = alias
            break
    order = cache.get('connection_order', [])
    order.append(connected_alias)
    cache.set('connection_order', order)

def limit_max_connections(sender, connection, **kwargs):
    databases = connections.databases
    aliases = Set(databases.keys())
    excluded = Set(MULTIDB_EXCLUDE_FROM_CLEANUP)
    disconnectable = aliases - excluded
    
    print 'New Connection.\tConnected: %s\tDisconnectable: %s\t%s' % (len(aliases), len(disconnectable), len(aliases) > MULTIDB_MAX_CONNECTIONS and 'Cleanup required' or '')
    
    while len(aliases) > MULTIDB_MAX_CONNECTIONS:
        alias = cleanup(disconnectable)
        
        if alias not in databases:
            raise Exception('Could not find connection alias %s' % alias)
        if alias in MULTIDB_EXCLUDE_FROM_CLEANUP:
            raise Exception('%s is in MULTIDB_EXCLUDE_FROM_CLEANUP' % alias)
            
        conn = connections[alias]
            
        if conn == connection:
            raise Exception('Attempt to disconnect %s, but disconnecting a new connection is not allowed' % alias)
        
        utils.disconnect(alias, connection=conn)
        aliases = Set(databases.keys())
        disconnectable = aliases - excluded
