from django.conf import settings


MULTIDB_MAX_CONNECTIONS = int(getattr(settings, 'MULTIDB_MAX_CONNECTIONS', 20))
MULTIDB_MAX_CONNECTIONS_MAPPING = dict(getattr(settings, 'MULTIDB_MAX_CONNECTIONS_MAPPING', {}))
MULTIDB_CLEANUP_FUNCTION = getattr(settings, 'MULTIDB_CLEANUP_FUNCTION', 'multidb.utils.inorder_cleanup')
MULTIDB_EXCLUDE_FROM_CLEANUP = tuple(getattr(settings, 'MULTIDB_EXCLUDE_FROM_CLEANUP', ('default', )))
MULTIDB_ALLOW_CURRENT_CONNECTION_CLEANUP = bool(getattr(settings, 'MULTIDB_ALLOW_CURRENT_CONNECTION_CLEANUP', False))
