#!/usr/bin/env python
#coding:utf-8
#author:albert
#date:2015-09-14

#基础mysql配置

#redis配置
# : we recommend that you connect to Redis via Twemproxy
SAMPLE_REDIS_CONFIG = {
    'default': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'password': None
    },
}

#基础cassandra配置
SAMPLE_CASSANDRA_HOSTS = ['127.0.0.1']
SAMPLE_CASSANDRA_KEYSPACES ='smaple'