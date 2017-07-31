#!/usr/bin/env python
# coding:utf-8
import pymysql, time


def select_mysql(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='UYCC3JpsVxcHElmTaiyR', db='zabbix',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet


def insert_mysql(sql):
    conn = pymysql.connect(host='121.201.7.63', port=33060, user='jiang', passwd='jiangwenhui', db='datashow',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet


if __name__ == "__main__":
    SSO_msql_sql = "select value,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i:%s' ) from zabbix.history WHERE   clock>=unix_timestamp(curdate()) and itemid=46701 order by clock desc limit 1;"
    SSO_msql_qps = select_mysql(SSO_msql_sql)[0][0]

    电商_msql_sql = "select value,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i:%s' ) from zabbix.history WHERE   clock>=unix_timestamp(curdate()) and itemid=46702 order by clock desc limit 1;"
    电商_msql_qps = select_mysql(电商_msql_sql)[0][0]

    insert_sql = "insert into app01_当前数据库qps(SSOMySQL,电商MySQL,times) values('{}','{}','{}')".format(round(SSO_msql_qps),
                                                                                                         round(电商_msql_qps),
                                                                                                         time.strftime(
                                                                                                             '%Y-%m-%d %H:%M:%S'))
    insert_mysql(insert_sql)
    print('ok')
