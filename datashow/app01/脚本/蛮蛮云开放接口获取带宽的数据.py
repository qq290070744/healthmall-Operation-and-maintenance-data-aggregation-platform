# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `python_demo`
    @Author : `MMY_long`
    @Date   : `2017-07-14`
    @About  : '获取带宽的数据的python Demo'
"""
import time
import urllib
import hashlib
import requests
import traceback
import json, pymysql
from collections import OrderedDict


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


def func(domain):
    # 安全密钥
    skey = "skey"
    # 用户唯一标识
    uuid = "uuid"
    # 域名
    domain = domain
    # API版本
    ver = "v1"
    # 接口地址
    url = "http://api.chinamaincloud.com/api/stat/getBandwidth"

    def generate_sign(params):
        """
        生成sign 签名
        :param params:
        :return:
        """
        params['params'] = json.dumps(params['params'], separators=(',', ':'))
        # 排序
        sort_dict = sorted(params.items(), key=lambda d: d[0])
        plain = ''
        for key, value in sort_dict:
            plain = plain + "|" + key + "=" + value
        plain = plain[1:] + "|" + skey
        m2 = hashlib.md5()
        m2.update(plain)
        sign = m2.hexdigest()
        params["sign"] = sign

    def get_params(start_time, end_time, interval='5m', unit='K'):
        """
        获取请求参数
        :param start_time:
        :param end_time:
        :param interval:
        :param unit:
        :return:
        """
        params = {
            "params": OrderedDict([
                ("domain", domain),
                ("startTime", start_time),
                ("endTime", end_time),
                ("interval", interval),
                ("unit", unit)
            ]),
            "uuId": uuid,
            "ver": ver,
            # 当前时间戳，单位（毫秒）
            "time": str(int(time.time()) * 1000)
        }
        generate_sign(params)
        return params

    try:
        data = get_params('{}0000'.format(time.strftime('%Y%m%d')), '{}2359'.format(time.strftime('%Y%m%d')))
        res = requests.post(url, data=data)
        outDatas = res.json()['data']['outDatas']
        for i in outDatas:
            # print i
            sql = "insert into app01_cdn_带宽 values(null,'{}','{}','{}')".format(i['value'], i['time'], domain)
            insert_mysql(sql)

    except Exception as e:
        print(traceback.format_exc(e))


domain_list = ["imgdata1.healthmall.cn", "imgdata2.healthmall.cn", "imgdata3.healthmall.cn",
               "activity.daxmall.com", "dxact.healthmall.cn", "fenxiang.healthmall.cn", "api.healthmall.cn"
               ]
if __name__=="__main__":
    insert_mysql("delete from app01_cdn_带宽 where times>='{}'".format(time.strftime('%Y%m%d')))
    for i in domain_list:
        func(i)
    print ('ok')
