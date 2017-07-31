#!/usr/bin/env python
#coding:utf-8
import pymysql,time
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

def main(alertid,alerttype):
    sql = "select count(*) from alerts where  clock>=unix_timestamp(curdate()) and message like '%{}%';".format(alerttype)
    # print(select_mysql(sql)[0][0])
    insert_mysql("insert into app01_告警情况 values (null,'{}','{}','{}','{}')".format(alertid,alerttype,select_mysql(sql)[0][0],time.strftime('%Y-%m-%d %H:%M:%S')))

if __name__=="__main__":
    insert_mysql("delete from app01_告警情况 where times>=curdate()")
    main(1,'Disaster')
    main(2,'High')
    main(3,'Average')