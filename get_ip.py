#!/usr/bin/env python
# coding=utf-8

from base.ipinfooperate import IpinfoOperater
from base.function import *
from base.config import *
from base.baselog import BaseLog
import time

globalLog=BaseLog(LOG_LEVEL,LOG_PATH,LOG_FILE,LOG_WHEN,LOG_BACKUPCOUNT,LOG_ROTATING_INTERVAL)
ipinfoOperater = IpinfoOperater(globalLog)

i = 16777216
while i <= 167772159:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
    i = i + 1


i = 184549376
while i <= 2130706431:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
    i = i + 1
i = 2147483648
while i <=2886729727:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    i = i + 1
    time.sleep(0.5)
i = 2887778304
while i <= 3221225471:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
    i = i + 1 
i = 3221225472
while i <= 3232235519:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
    i = i + 1
i = 3232301056
while i <= 3758096383:
    ip = ip_iton(i)
    ipinfoOperater.set_ipinfo(ip)
    time.sleep(0.5)
    i = i + 1
