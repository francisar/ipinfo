#!/usr/bin/env python
# coding=utf-8

from base.ipinfooperate import IpinfoOperater
from base.function import *
from base.config import *
import time

globalLog=BaseLog(LOG_LEVEL,LOG_PATH,LOG_FILE,LOG_WHEN,LOG_BACKUPCOUNT,LOG_ROTATING_INTERVAL)
ipinfoOperater = IpinfoOperater(globalLog)


for i in range(16777216,167772159):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)



for i in range(184549376,2130706431):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
for i in range(2147483648,2886729727):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
for i in range(2887778304,3221225471):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
for i in range(3221225472,3232235519):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
for i in range(3232301056,3758096383):
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
