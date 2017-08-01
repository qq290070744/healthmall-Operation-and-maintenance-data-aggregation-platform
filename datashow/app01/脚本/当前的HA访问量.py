#!/usr/bin/env python
#coding:utf-8
import pymysql


def select_mysql(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='passwd', db='zabbix',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet


def insert_mysql(sql):
    conn = pymysql.connect(host='121.201.7.63', port=3306, user='user', passwd='passwd', db='datashow',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet

if __name__=="__main__":
    select_sql = "SELECT value,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i:%s' ) FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate()) and itemid in (29535) order by clock desc limit 1;"
    select_data = select_mysql(select_sql)[0]
    # print(select_data)
    insert_sql = "insert into app01_当前的ha访问量 values(null,'{}','{}')".format(select_data[0],select_data[1])
    insert_mysql(insert_sql)
    print(insert_sql)
