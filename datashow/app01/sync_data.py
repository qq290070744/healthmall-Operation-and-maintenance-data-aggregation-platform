#!/usr/bin/env python
#coding:utf-8

# unix_timestamp(curdate())

# SELECT SUM(value),itemid FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate()) and itemid in (25361) group by itemid;
# SELECT SUM(value),itemid,FROM_UNIXTIME( clock, '%Y-%m-%d' ) FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate()) and itemid in (25361) group by itemid,FROM_UNIXTIME( clock, '%Y-%m-%d' );
# SELECT SUM(value),itemid,FROM_UNIXTIME( clock, '%Y-%m-%d' ) FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate())-65535*7 and itemid in (25361) group by itemid,FROM_UNIXTIME( clock, '%Y-%m-%d' );
# SELECT SUM(value),itemid,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' ) FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate()) and itemid in (25361) group by itemid,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' );
# SELECT itemid,SUM(VALUE), FROM_UNIXTIME(min(clock), '%Y-%m-%d %H:%i'), clock div 300 FROM zabbix.history_uint WHERE clock >= unix_timestamp(curdate()) AND itemid IN (25361) GROUP BY itemid, clock div 300;
# SELECT SUM(VALUE), itemid, FROM_UNIXTIME(min(clock), '%Y-%m-%d %H:%i') FROM zabbix.history_uint WHERE clock >= unix_timestamp(curdate()) AND itemid IN (25361) GROUP BY itemid, clock div 300;
# SELECT value*1000,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' ) FROM zabbix.history WHERE   clock>=unix_timestamp(curdate()) and itemid in (46370) order by clock desc limit 1;