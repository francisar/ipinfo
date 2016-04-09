#!/usr/bin/env python
# coding=utf-8
from function import Config



cf = Config()
LOG_FILE = cf.get('logging','log_file')

LOG_PATH = cf.get('logging','log_path')
LOG_LEVEL = cf.get('logging','log_level')
LOG_WHEN = cf.get('logging','log_when')
LOG_BACKUPCOUNT = cf.get('logging','log_backupCount')
LOG_ROTATING_INTERVAL = cf.get('logging','log_rotating_interval')
LOG_QUEUELEN = cf.get('logging','log_queuelen')


DBHOST =  cf.get('db','host')
DBPORT = cf.get('db','port')
DBUSER = cf.get('db','user')
DBPASSWD = cf.get('db','passwd')
DBNAME = cf.get('db','dbname')


