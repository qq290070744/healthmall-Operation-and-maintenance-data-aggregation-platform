# !/usr/bin/env python
# -*- coding:utf-8 -*-
# redis命中率
import redis,pymysql,time


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


def func(host, port):
    pool = redis.ConnectionPool(host=host, port=port)
    r = redis.Redis(connection_pool=pool)
    info = r.info()
    hits = float(info['keyspace_hits'])
    miss = float(info['keyspace_misses'])
    Hit_rate = hits / (hits + miss) * 100
    return Hit_rate


Electricity_business = {
    '10.0.5.200': 30201,
    '10.0.5.201': 30202,
    '10.0.5.202': 30203,
    '10.0.5.203': 30204,
    '10.0.5.204': 30205,
    '10.0.5.205': 30206,
}

NET = {
    '10.0.5.200': 30001,
    '10.0.5.201': 30002,
    '10.0.5.202': 30003,
    '10.0.5.203': 30004,
    '10.0.5.204': 30005,
    '10.0.5.205': 30006,
}

SSO = {
    '10.0.5.200': 30101,
    '10.0.5.201': 30102,
    '10.0.5.202': 30103,
    '10.0.5.203': 30104,
    '10.0.5.204': 30105,
    '10.0.5.205': 30106,
}


def get_Hit_rate(business):
    Hit_rate = 0
    for k, v in business.items():
        Hit_rate += func(k, v)
    Hit_rate = round(Hit_rate / len(business), 2)
    return Hit_rate


Electricity_business_Hit_rate = get_Hit_rate(Electricity_business)
NET_Hit_rate = get_Hit_rate(NET)
SSO_Hit_rate = get_Hit_rate(SSO)


if __name__=="__main__":
    insert_sql="insert into app01_redis命中率 values(null,'{}','{}','{}','{}')".format(Electricity_business_Hit_rate,NET_Hit_rate,SSO_Hit_rate,time.strftime('%Y-%m-%d %H:%M:%S'))
    insert_mysql(insert_sql)
    print(insert_sql)