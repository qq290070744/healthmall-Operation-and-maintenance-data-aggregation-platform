#!/usr/bin/env python
# coding:utf-8
import requests, os, json, time

url = 'http://fusion.qiniuapi.com/v2/tune/bandwidth'
payload = {
    "startDate": time.strftime('%Y-%m-%d 00:00:00'),
    "endDate": time.strftime('%Y-%m-%d %H:%M:%S'),
    "granularity": '5min',
    "domains": ''
}

headers = {'content-type': 'application/json', 'Authorization': ''}

ret = requests.post(url, data=json.dumps(payload), headers=headers)

print(ret.text)
