#!/usr/bin/env python
# coding:utf-8
import qingcloud.iaas, json, pymysql, time


def insert_mysql(sql):
    conn = pymysql.connect(host='121.201.7.63', port=33060, user='user', passwd='passwd', db='datashow',

                           charset='UTF8')

    cur = conn.cursor()

    cur.execute(sql)
    nRet = cur.fetchall()
    conn.commit()

    cur.close()

    conn.close()
    return nRet


def main(qy_access_key_id, qy_secret_access_key):
    def func(节点id):
        conn = qingcloud.iaas.connect_to_zone(
            节点id,
            
            qy_access_key_id,
            qy_secret_access_key,
        )

        host_list = conn.describe_instances()
        主机总数 = 0
        for i in host_list['instance_set']:
            if i['status'] != 'ceased':
                # if i['status'] != 'ceased':
                主机总数 += 1
                # print(i['status'])
        # print(主机总数)
        # for i in host_list['instance_set'] :
        #     print(i['owner'])
        硬盘列表 = conn.describe_volumes()
        硬盘总数 = 0
        for i in 硬盘列表['volume_set']:
            if i['status'] != 'ceased':
                硬盘总数 += 1
        # print(硬盘总数)
        路由器列表 = conn.describe_routers()
        路由器总数 = 0
        for i in 路由器列表['router_set']:
            if i['status'] != 'ceased':
                路由器总数 += 1
        # print(路由器总数)
        公网IP列表 = conn.describe_eips()
        公网IP总数 = 0
        for i in 公网IP列表['eip_set']:
            if i['status'] != 'ceased':
                公网IP总数 += 1
        # print(公网IP总数)
        return {"主机总数": 主机总数, "硬盘总数": 硬盘总数, "路由器总数": 路由器总数, "公网IP总数": 公网IP总数}

    节点id_list = ['PEK3A', 'GD1', 'SH1A']
    主机总数 = 0
    硬盘总数 = 0
    路由器总数 = 0
    公网IP总数 = 0
    for i in 节点id_list:
        dic = func(i)
        主机总数 += dic['主机总数']
        硬盘总数 += dic['硬盘总数']
        路由器总数 += dic['路由器总数']
        公网IP总数 += dic['公网IP总数']
    # print(主机总数, 路由器总数, 硬盘总数, 公网IP总数)
    return {"主机总数": 主机总数, "路由器总数": 路由器总数, "硬盘总数": 硬盘总数, "公网IP总数": 公网IP总数}


key_dic = {"....": "....",
           "....": "....",
           "....":"....",
           "....":"....",
           "....":"...."
           }
if __name__ == "__main__":
    主机总数 = 0
    路由器总数 = 0
    硬盘总数 = 0
    公网IP总数 = 0
    for k, v in key_dic.items():
        ret_dic = main(k, v)
        主机总数 += ret_dic['主机总数']
        路由器总数 += ret_dic['路由器总数']
        硬盘总数 += ret_dic['硬盘总数']
        公网IP总数 += ret_dic['公网IP总数']
    print(主机总数, 路由器总数, 硬盘总数, 公网IP总数)
    insert_mysql("insert into app01_青云用量 values (null,'{}','{}','{}','{}','{}')"
                 .format(主机总数, 路由器总数, 硬盘总数, 公网IP总数, time.strftime('%Y-%m-%d %H:%M:%S'))
                 )
