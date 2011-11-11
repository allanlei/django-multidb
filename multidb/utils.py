from django.db import connections
from django.core.cache import cache

from random import choice


def random_cleanup(aliases, **kwargs):
    return choice(list(aliases))

def inorder_cleanup(aliases, **kwargs):
    order = cache.get('connection_order', [])
    alias = order.pop(0)
    
    cache.set('connection_order', order)
    if alias:
        return alias
    return choice(list(aliases))
    
def disconnect(alias, connection=None, delete=True):
    print 'Disconnecting %s' % alias
    if connection is None:
        connection = connections[alias]

    connection.close()
    if delete:
        del connections.databases[alias]
