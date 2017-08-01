#!/usr/bin/env python
# coding:utf-8
import pymysql


def select_mysql(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='passwd', db='zabbix',

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


def main(in_or_out,itemid):
    select_sql = "SELECT itemid,SUM(VALUE),  FROM_UNIXTIME(min(clock), '%Y-%m-%d %H:%i') FROM zabbix.history_uint WHERE clock >= unix_timestamp(curdate()) AND itemid IN ({}) GROUP BY itemid, clock div 300;".format(itemid)
    select_data = select_mysql(select_sql)
    for i in select_data:
        insert_sql = "insert into app01_总流量 values(null,'{}','{}','{}','{}')".format(i[0], i[1], i[2], in_or_out)
        insert_mysql(insert_sql)



if __name__ == "__main__":
    insert_mysql("delete from app01_总流量 WHERE times >= curdate();")
    main('in',25361)
    main('out',25544)
