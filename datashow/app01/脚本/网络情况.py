#!/usr/bin/env python
#coding:utf-8
import pymysql,time
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

if __name__=="__main__":
    itemid_li=[46382,46454]
    sql="SELECT value*1000,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' ) FROM zabbix.history WHERE   clock>=unix_timestamp(curdate()) and itemid in ({}) order by clock desc limit 1;"
    insert_mysql("insert into app01_网络情况 values(null,'{}','{}','{}','{}','{}','{}','{}')".format(select_mysql(sql.format(46382))[0][0],select_mysql(sql.format(46454))[0][0],'N/A',time.strftime('%Y-%m-%d %H:%M:%S'),'N/A','N/A','N/A'))
    print('ok')
