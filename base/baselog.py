#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler
from function import switch
#from logging.handlers import RotatingFileHandler
#log_file_handler = TimedRotatingFileHandler(filename="ds_update", when="M", interval=2, backupCount=2)

class BaseLog(object):

	_level = {
		'CRITICAL': logging.CRITICAL,
		'DEBUG': logging.DEBUG,
		'ERROR': logging.ERROR,
		'FATAL': logging.FATAL,
		'WARNING': logging.WARNING,
		'WARN': logging.WARN,
		'INFO': logging.INFO,
		'NOTSET': logging.NOTSET
	}

	def __init__(self,log_level,log_path,log_when,log_backupCount,log_rotating_interval,name=__name__):
                log_format = '%(asctime)s %(levelname)s %(threadName)s %(filename)s[line:%(lineno)d] %(message)s'
		self._logger = logging.getLogger(name)
		self._logger.setLevel(self._level[log_level.upper()])
		for h in self._logger.handlers:
			self._logger.removeHandler(h)
		handler = TimedRotatingFileHandler(filename=log_path, when=log_when, interval=eval(log_rotating_interval), backupCount=eval(log_backupCount))
		#handler = logging.FileHandler(log_path)
		handler.setLevel(self._level[log_level.upper()])
		formatter = logging.Formatter(log_format)
		handler.setFormatter(formatter)
		self._logger.addHandler(handler)
	
	def writelog(self,log_level,message):
		for case in switch(log_level.strip().lower()):
			if case('warn'):
				self.warn(message)
				break
			if case('info'):
				self.info(message)
				break
			if case('error'):
				self.error(message)
				break
			if case('debug'):
				self.debug(message)
				break
			if case():
				break

	def info(self, message):
		self._logger.info(message)

	def warn(self, message):
		self._logger.warn(message)

	def error(self, message):
		self._logger.error(message)

	def debug(self, message):
		self._logger.debug(message)
