#!/usr/bin/env python
# coding:utf-8
import pymysql, time


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


def ret_sql(itemid):
    sql = "SELECT value*1000,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' ) FROM zabbix.history WHERE   clock>=unix_timestamp(curdate()) and itemid in ({}) order by clock desc limit 1;".format(
        itemid)
    data = select_mysql(sql)[0][0]
    return data


def ret_status(itemid):
    sql = "SELECT value,FROM_UNIXTIME( clock, '%Y-%m-%d %H:%i' ) FROM zabbix.history_uint WHERE   clock>=unix_timestamp(curdate()) and itemid in ({}) order by clock desc limit 1;".format(
        itemid)
    return select_mysql(sql)[0][0]


def main():
    insert_mysql(
        "insert into app01_服务响应时间和当前状态 values(null,'{}','{}','{}','{}','{}','{}')".format("后台API", ret_sql(46370),
                                                                                          ret_sql(46460),
                                                                                          ret_status(46461),
                                                                                          ret_status(46371),
                                                                                          time.strftime(
                                                                                              '%Y-%m-%d %H:%M:%S')))
    insert_mysql(
        "insert into app01_服务响应时间和当前状态 values(null,'{}','{}','{}','{}','{}','{}')".format("登陆", ret_sql(46407),
                                                                                          ret_sql(46472),
                                                                                          ret_status(46473),
                                                                                          ret_status(46408),
                                                                                          time.strftime(
                                                                                              '%Y-%m-%d %H:%M:%S')))
    insert_mysql(
        "insert into app01_服务响应时间和当前状态 values(null,'{}','{}','{}','{}','{}','{}')".format("电商首页", ret_sql(46395),
                                                                                          ret_sql(46466),
                                                                                          ret_status(46467),
                                                                                          ret_status(46396),
                                                                                          time.strftime(
                                                                                              '%Y-%m-%d %H:%M:%S')))


if __name__ == "__main__":
    main()
    print('ok')
