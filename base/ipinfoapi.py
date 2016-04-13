#!/usr/bin/python
#coding=utf-8

'''
#=============================================================================
#
#     FileName: ipinfoapi.py
#         Desc: 获取Ip相关信息的api
#
#       Author:francis
#
#      Created: 2014-4-5 
#      Version: 1.0.0
#      History:
#               1.0.0 | francis
#
#=============================================================================
'''

import copy
import json
import requests

#from common.sns_network  import SNSNetwork

#OPEN_HTTP_TRANSLATE_ERROR = 1801

class IpinfoApi(object):

    def __init__(self,logger,iplist='http://ip.taobao.com'):
        super(IpinfoApi, self).__init__()
        self.__ip = iplist
        self.__logger = logger

    def call(self,  ip, url_path='/service/getIpInfo.php', method='get'):
        '''
        调用接口，并将数据格式转化成json
        只需要传入pf, openid, openkey等参数即可，不需要传入sig
        format即使传xml也没有用，会被强制改为json
        '''
        uri = "%s%s?ip=%s" % (self.__ip,url_path,ip)
        try:
            request = requests.get(uri,
                    headers={"Content-Type" : \
                    "application/json", "Accept" : "application/json"}, timeout=10)
            self.__logger.write("debug","url:%s,status:%d"%(uri,request.status_code))
            if request.status_code <> 200:
                self.__logger.write("error","connect url %s faild %d,params:%s"%(uri,request.status_code,ip))
                return {}
            return json.loads(request.content)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout), msg:
            self.__logger.write("error","URLERROR-%s,params:%s"%(msg,str(ip)))
            return {}


    def getipinfo(self, ip):
        jdata = self.call(ip)
        return jdata


#a = IpinfoApi()
#print a.getipinfo('203.195.183.146')
