from cassandra.cluster import Cluster

import settings

def setup_connection():
    connection.setup(
        hosts=settings.STREAM_CASSANDRA_HOSTS,
        consistency=settings.STREAM_CASSANDRA_CONSISTENCY_LEVEL,
        default_keyspace=settings.STREAM_DEFAULT_KEYSPACE,
        **settings.CASSANDRA_DRIVER_KWARGS
    )
