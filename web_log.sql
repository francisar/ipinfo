# Host: 172.16.1.1:33060  (Version: 5.6.26)
# Date: 2015-10-10 15:06:34
# Generator: MySQL-Front 5.3  (Build 4.214)

/*!40101 SET NAMES utf8 */;
CREATE DATABASE `ipinfo` DEFAULT CHARACTER SET utf8; /*!40100 DEFAULT CHARACTER SET utf8 */

use ipinfo;
#
# Structure for table "ipinfo"
#

DROP TABLE IF EXISTS `ipinfo`;
CREATE TABLE `ipinfo` (
  `ipaddr` char(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `country` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `province` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `isp` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ipaddr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

#
# Data for table "ipinfo"
#



