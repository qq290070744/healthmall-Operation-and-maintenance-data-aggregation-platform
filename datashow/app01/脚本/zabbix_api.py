#!/usr/bin/env python
# coding:utf-8
import requests, pymysql, json

payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "jwh",
        "password": "290070744"
    },
    "id": 1,
    "auth": None
}

headers = {'content-type': 'application/json'}
url="http://121.201.72.168:38888/api_jsonrpc.php"
ret = requests.post(url, data=json.dumps(payload), headers=headers)
auth=json.loads(ret.text)["result"]
print(auth)






